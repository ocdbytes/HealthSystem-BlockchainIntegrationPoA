from time import time
from Functions.provider import Provider
import json
from web3 import Web3
from solcx import compile_standard, install_solc

install_solc("0.8.0")
# Main Address Config (Ganache)
'''
Chain ID
--------

POLYGON(Mumbai) : 80001
ETH(Groeli) : 5
'''
main_config = {
    "chain_id": 5,
    "my_address": "WALLET ADDRESS",
    "my_private_key": "WALLET PRIVATE KEY"
}


# ABIs
with open("./Assets/ProviderCompiled.json", "r") as f:
    ProviderCompiled = json.load(f)


def main():
    providerObject = Provider(
        main_config["my_address"], ProviderCompiled, main_config["my_private_key"])


if __name__ == "__main__":
    main()
