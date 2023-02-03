// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.17;

contract SMSOracle {

// Event that is emitted when the oracle should send an SMS
    event SendSMS(
        string  phoneNumber,
        string  message
    );

   // A flag to track whether the oracle is currently sending an SMS
    bool private sendingSMS;

// Function that can be called to trigger the oracle to send an SMS
    function requestSMS(string memory phoneNumber, string memory message) public {
        // Make sure the oracle is not currently sending an SMS       
        require(!sendingSMS);

        // Set the flag to indicate that the oracle is now sending an SMS
        sendingSMS = true;

         // Emit the SendSMS event
        emit SendSMS(phoneNumber, message);

        // Clear the flag to indicate that the oracle is no longer sending an SMS
        sendingSMS = false;
    }
}