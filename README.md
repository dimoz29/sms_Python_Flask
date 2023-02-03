#we need to compile, test, debug, and deploy our contracts.

#First make sure you have node version 12 or above and npm installed. Then install Hardhat.
```
node --version
npm --version
```
#If you don't have node you can find the installaiton guides for Windows, macOS, and Linux here:  https://nodejs.org/en/download/

```
mkdir sms-test
cd sms-test
npm init -y
npm install dotenv
npm install --save-dev hardhat
```
```
npx hardhat
```
#click yes to all

Set up POKT https://app.cadena.dev/ZHjzLozd3mCsAcgMfeHE/lesson/ethereum-101/lesson-eth-6/6
```
npx hardhat compile
```
```
npx hardhat run scripts/deploy.js --network goerli
```
you will end up with s/th like that
```
SMSOracleContract deployed to: 0x006202d2E96abeb270beAba53aBeE242f3353Af9
SMSOracleContract owner address: 0xc3Be43715114CC06664e1f49E12C472C3BDb9cE8
```
you can see the transaction on Etherscan if you visit https://goerli.etherscan.io/address/ and search with your address.
