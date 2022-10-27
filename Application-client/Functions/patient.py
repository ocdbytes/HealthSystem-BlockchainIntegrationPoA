import os
import json
import string
from web3 import Web3
from solcx import compile_standard, install_solc
import time
import csv


class Main:
    def __init__(self, address: string, abi, privateKey: string):
        self.address = address
        self.privateKey = privateKey
        self.w3 = Web3(Web3.HTTPProvider(
            "https://goerli.infura.io/v3/9e47bc5ab190496aa6ea8cba79719d7a"))
        print("Blockchain Connected.... 📦🔗")
        self.Main = self.w3.eth.contract(
            address="0xC9de7bbE283D5D11614d3450c2f583bfBE3c4aaB", abi=abi)
        print("------------------------------------------------------------")
        print("Contract for [PATIENT/USER] interaction initialised ✅")
        print("------------------------------------------------------------")
        # ---------------------------[CSV]---------------------------
        # fields = ["ProviderContractInitialisation&Connection",
        #           f"{et-st}", 'Ethereum Goerli']
        # with open('./main_ethereum.csv', 'a', newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(fields)
        #     f.close()
        # -----------------------------------------------------------
        self.OptionScreen()

    # Transaction Process
    # -------------------

    # 1. Build a Transaction
    # 2. Sign a Transaction
    # 3. Send a Transaction

    def OptionScreen(self):
        print('''------------------------[PATIENT'S SCREEN]------------------------
1. Get Self Keys
2. Check If Patient Exists (PROVIDER FUNCTION)
3. Add Patient (PROVIDER FUNCTION)
q. Quit
-------------------------------------------------------------------
        ''')
        opt = input("Select Option > ")
        if(opt == "1"):
            self.GetSelfKeys()
        elif(opt == "2"):
            self.CheckIfPatientExists()
        elif(opt == "3"):
            self.AddPatientToDatabase()
        elif(opt == "q"):
            exit(1)
        else:
            print("Please select a valid option !!!")
            self.OptionScreen()

    def GetSelfKeys(self):
        n = self.w3.eth.getTransactionCount(self.address)
        print("------------------------[SELF KEYS]------------------------")
        transaction = self.Main.functions.getSelfKeys().buildTransaction({
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
        print(f"Your Key [{self.address}] :")
        print(self.Main.functions.getSelfKeys().call())
        print("------------------------------------------------------------")
        self.OptionScreen()

    def CheckIfPatientExists(self):
        n = self.w3.eth.getTransactionCount(self.address)
        print(
            "------------------------[CHECK IF PATIENTS EXISTS]------------------------")
        addr = input("Address > ")
        transaction = self.Main.functions.checkPatient(addr).buildTransaction({
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
        print("-------------------------------------------------------------------------")
        res = self.Main.functions.checkPatient(addr).call()
        if(res == True):
            print(f"Yes, Patient with address : {addr} exists in DB")
        else:
            print(f"No, Patient with address : {addr} doesn't exists in DB")
        print("-------------------------------------------------------------------------")
        self.OptionScreen()

    def AddPatientToDatabase(self):
        n = self.w3.eth.getTransactionCount(self.address)
        print(
            "------------------------[ADD PATIENT]------------------------")
        name = input("Patient Address > ")
        key = input("Access Key > ")
        transaction = self.Main.functions.addPatientToDatabase(name, key).buildTransaction({
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
        print(f"Patient : {name} added successfully with Key : {key}")
        print("------------------------------------------------------------")
        self.OptionScreen()
