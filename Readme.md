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

**Proposed Architecture for the System**

<p align="center">
<img src="./Readme_images/1.png" width="50%"></img>
</p>

**OUR ARCHITECTURE & DATA FLOW with entities 👷🚀**

<p align="center">
<img src="./Readme_images/NewDiagram.png" width="50%"></img>
</p>

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

From here we can observe that our contract has no errors or so we will now deploy our contract on two different networks.

- Polygon Mumbai Testnet
- Ethereum Goerli Testnet

### We will use Remix IDE to deploy the contracts to the Test nets

**POLYGON**

---

- Provider.sol → `0x924bDF9655e84a65Cb9Af6431Ac9E7Eb04A550f8`
- Main.sol → `0x19f10b2E9E1fC1D57Af3F489Fb78A5463b6ffF82`

**GOERLI**

---

- Provider.sol → `0x908131D2ED45370ba51c578b9E2003f37b82E13b`
- Main.sol → `0xC9de7bbE283D5D11614d3450c2f583bfBE3c4aaB`

Contracts Deployed ✅ on Blockchain (Polygon Mumbai & Ethereum Goerli) 📦
