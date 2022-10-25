import os
import json
import string
from web3 import Web3
from solcx import compile_standard, install_solc


class Patient:
    def __init__(self, address: string):
        self.address = address

    # Transaction Process
    # -------------------

    # 1. Build a Transaction
    # 2. Sign a Transaction
    # 3. Send a Transaction
