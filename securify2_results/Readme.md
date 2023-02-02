# Securify 2

Docker Installation :

```txt
git clone https://github.com/eth-sri/securify2
cd securify2
nano Dockerfile -> [change SOLC version to 0.8.7] -> save
sudo docker build -t securify .
```

Running Tool :
```txt
sudo docker run -it -v <contract/directory/full/path>:/share securify /share/main.sol

Eg : 
sudo docker run -it -v /Users/family/Desktop/BlockChain/HealthSystem-BlockchainIntegrationPoA/Contract/contracts:/share securify /share/main.sol
```
