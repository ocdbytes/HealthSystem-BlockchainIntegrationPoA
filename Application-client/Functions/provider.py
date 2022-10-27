import os
import json
import string
import time
from web3 import Web3
from solcx import compile_standard, install_solc
import csv


class Provider:

    def __init__(self, address: string, abi, privateKey: string):
        self.address = address
        self.privateKey = privateKey
        self.w3 = Web3(Web3.HTTPProvider(
            "https://goerli.infura.io/v3/9e47bc5ab190496aa6ea8cba79719d7a"))
        print("Blockchain Connected.... 📦🔗")
        self.Provider = self.w3.eth.contract(
            address="0x908131D2ED45370ba51c578b9E2003f37b82E13b", abi=abi)
        print("------------------------------------------------------------")
        print("Contract for [PROVIDER] interaction initialised ✅")
        print("------------------------------------------------------------")

        # # --------------------CSV Code-----------------------
        # fields = ["ProviderContractInitialisation&Connection",
        #           f"{et-st}", 'Polygon Mumbai']
        # with open('./providers_polygon.csv', 'a', newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(fields)
        #     f.close()
        # # --------------------CSV Code-----------------------

        self.OptionsScreen()

    # Transaction Process
    # -------------------

    # 1. Build a Transaction
    # 2. Sign a Transaction
    # 3. Send a Transaction

    def OptionsScreen(self):
        print('''------------------------[PROVIDER'S SCREEN]------------------------
1. Get Self Info
2. Get Contract Owner
3. Add Provider (OWNER FUNCTION)
q. Quit
-------------------------------------------------------------------
        ''')
        opt = input("Select Option > ")
        if(opt == "1"):
            self.GettingSelfInfo()
        elif(opt == "2"):
            self.GetOwner()
        elif(opt == "3"):
            self.AddProvider()
        elif(opt == "q"):
            exit(1)
        else:
            print("Please Select from the options avialable above!!!!")
            self.OptionsScreen()

    def GettingSelfInfo(self):
        n = self.w3.eth.getTransactionCount(self.address)
        print("------------------------[SELF INFO]------------------------")
        print("Your Address : ", self.address)
        transaction = self.Provider.functions.checkIfProvider(self.address).buildTransaction({
            "chainId": 5,
            "from": self.address,
            "nonce": n,
            "gasPrice": self.w3.eth.gas_price
        })
        signed_transaction = self.w3.eth.account.sign_transaction(
            transaction, private_key=self.privateKey
        )
        send_transaction = self.w3.eth.send_raw_transaction(
            signed_transaction.rawTransaction)
        transaction_recipt = self.w3.eth.wait_for_transaction_receipt(
            send_transaction)
        print("Are you a Provider ? : ",
              self.Provider.functions.checkIfProvider(self.address).call())
        print("------------------------------------------------------------")
        self.OptionsScreen()

    def GetOwner(self):
        print("--------------------[CONTRACT'S OWNER]----------------------")
        print("Provider Contract Owner Address : ",
              self.Provider.functions.owner().call())
        print("------------------------------------------------------------")
        self.OptionsScreen()

    def AddProvider(self):
        print("----------------------[ADD PROVIDER]------------------------")
        n = self.w3.eth.getTransactionCount(self.address)
        inp = input("Enter the Address(to be added as provider) > ")
        transaction = self.Provider.functions.setProvider(inp).buildTransaction({
            "chainId": 5,
            "from": self.address,
            "nonce": n,
            "gasPrice": self.w3.eth.gas_price
        })
        signed_transaction = self.w3.eth.account.sign_transaction(
            transaction, private_key=self.privateKey
        )
        send_transaction = self.w3.eth.send_raw_transaction(
            signed_transaction.rawTransaction)
        transaction_recipt = self.w3.eth.wait_for_transaction_receipt(
            send_transaction)
        print("Transaction Recipt\n--------------------")
        print(transaction_recipt)
        print("------------------------------------------------------------")
        print(f"Address [{inp}] is added as a provider!!! 👨‍💻💼")
        print("------------------------------------------------------------")
        self.OptionsScreen()
