import os
import json
import string
from web3 import Web3
from dotenv import load_dotenv
from solcx import compile_standard, install_solc
install_solc("0.8.0")

load_dotenv()

# TEMP KEYS
main_config = {
    "chain_id": 1337,
    "my_address": "0x66aB6D9362d4F35596279692F0251Db635165871",
    "my_private_key": "0xbbfbee4961061d506ffbb11dfea64eba16355cbf1d9c29613126ba7fec0aed5d"
}

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
print("-----------------------------------------------------------------------------")
print("Connected to the blockchain 📦 ........")
print("-----------------------------------------------------------------------------")


def deployContract(contract_file: string, contract_class: string):
    # Reading the provider contract
    with open(f"../contracts/{contract_file}.sol") as f:
        file = f.read()

    compiled_contract = compile_standard({
        "language": "Solidity",
        "sources": {f"{contract_file}.sol": {"content": file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
                }
            }
        }
    },
        solc_version="0.8.0",
    )

    with open(f"./compiled_{contract_class}.json", 'w') as f:
        json.dump(compiled_contract, f)

    bytecode = compiled_contract["contracts"][f"{contract_file}.sol"][
        f"{contract_class}"]["evm"]["bytecode"]["object"]
    abi = compiled_contract["contracts"][f"{contract_file}.sol"][f"{contract_class}"]["abi"]

    # Connect to Ganache

    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    print(f"{contract_class} Contract generated using ABI & Bytecode ...........")

    # Get latest transaction
    nonce = w3.eth.getTransactionCount(main_config["my_address"])
    print(f"Total transactions done by {main_config['my_address']} : ", nonce)

    # 1. Build a Transaction
    # 2. Sign a Transaction
    # 3. Send a Transaction

    transaction = Contract.constructor().buildTransaction({
        "chainId": main_config["chain_id"],
        "from": main_config["my_address"],
        "nonce": nonce,
        "gasPrice": w3.eth.gas_price
    })

    print(f"Transaction build for {contract_class} is successful 🎯")

    # signing the transaction
    signed_transaction = w3.eth.account.sign_transaction(
        transaction, private_key=main_config["my_private_key"])

    # sending the signed transaction
    transaction_hash = w3.eth.send_raw_transaction(
        signed_transaction.rawTransaction)

    # wait for block confirmations
    transaction_recipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print(transaction_recipt)
    print("Transaction success ✅")
    return transaction_recipt.contractAddress


def updateAddressInMain(addressOfProvider: string):
    with open("../contracts/main.sol", 'r') as f:
        data = f.readlines()
    data[51] = f"            IProvider({addressOfProvider})"
    with open("../contracts/main.sol", 'w') as f:
        f.writelines(data)
    print("Address of Provider Contract in Main is Edited ✅ ........")


def main():
    ProviderContractAddress = deployContract("provider", "Provider")
    print("-----------------------------------------------------------------------------")
    print(f"PROVIDERS CONTRACT ADDRESS : {ProviderContractAddress}")
    print("-----------------------------------------------------------------------------")
    updateAddressInMain(ProviderContractAddress)
    MainContractAddress = deployContract("main", "Main")
    print("-----------------------------------------------------------------------------")
    print(f"MAIN CONTRACT ADDRESS : {MainContractAddress}")
    print("-----------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
