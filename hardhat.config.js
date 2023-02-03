require('@nomiclabs/hardhat-waffle');
require('dotenv').config();

module.exports = {
  solidity: "0.8.17",
  networks: {
    goerli: {
      url: `${process.env.POKT_Goerli_URL}`,
      accounts: [`${process.env.Goerli_PRIVATE_KEY}`],
    } 
  }
};
