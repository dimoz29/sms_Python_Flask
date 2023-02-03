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
