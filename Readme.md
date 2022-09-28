# Secure Blockchain Integration (Healthcare Systems)

Faculty : Ms. Sowmiya B

**E-Healthcare system in cloud computing using blockchain and medchain technology to protect user data.**

### System Architecture

- Our system will store all the patients data on the Cloud Network.
- There will be different nodes:
  - Patient’s Node
  - Provider’s Node
- There will be a key associated with every medical record, If we want to share the patient’s data then patient needs to share the key to access the medical records.
- The data stored in cloud is encrypted using asymmetric keys.

```
Cloud Structure : To store the data of the patients.
|
API : Acts as a Bridge for the data transfer
|
Blockchain : To create a safe access to the EMR using keys.
|
Nodes : To fetch the data from the Blockchain.
```

### Creating an Architecture

- Blockchain Smart Contracts
- Cloud Integrations

<p align="center">
<img src="./Readme_images/1.png" width="50%"></img>
</p>

Proposed Architecture for the system.

### Contracts :

Main.sol : It is a contract that acts as a bridge for the Provider Node and the Patient Node.

Provider.sol : It only keeps the record for Providers on the network as some features are only limited to the Provider in our main smart contract.

## Deployment :

### Contracts :

The deployment is being done on the Ganache Network for testing purposes and we are using python scripts to generate the compiled code for our solidity contract in order to get the ABI and the byte code to further access the functions of the Contract in a python script.

- Web3 : used to connect to the ganache interface
- solcx : To compile the contract

**Ganache Board :**

<img src="./Readme_images/2.png"></img>

**Compilation Output :**

<img src="./Readme_images/3.png"></img>
