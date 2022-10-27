from time import time
from Functions.provider import Provider
from Functions.patient import Main
import json
from web3 import Web3
from solcx import compile_standard, install_solc

install_solc("0.8.0")


# Main Address Config
'''
Chain ID
--------

POLYGON(Mumbai) : 80001
ETH(Groeli) : 5
'''

main_config = {
    "chain_id": 5,
    "my_address": "0x839F42a69Cc24F391DC4F09273f494578653edEC",
    "my_private_key": "6e96bd2242a939fe98149cc8e736170555cbd32e102e2d52fe1d004ac04eb356"
}


# ABIs
with open("./Assets/ProviderCompiled.json", "r") as f:
    ProviderCompiled = json.load(f)

with open("./Assets/MainCompiled.json", "r") as f:
    MainCompiled = json.load(f)


def main():
    print('''----------------------[WELCOME]----------------------
Welcome to the Healthcare application on Blockchain 👨‍⚕️🚑. 
Please select one of the options below to continue :
1. Main
2. Provider
q. Exit
----------------------------------------------------
    ''')
    opt = input("Option > ")
    if(opt == "2"):
        providerObject = Provider(
            main_config["my_address"], ProviderCompiled, main_config["my_private_key"])
    elif(opt == "1"):
        mainObject = Main(main_config["my_address"],
                          MainCompiled, main_config["my_private_key"])
    elif(opt == "q"):
        exit(1)


if __name__ == "__main__":
    main()
