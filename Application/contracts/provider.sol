// SPDX_License_Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

import "./main.sol";

contract Provider {
    /*
    PROVIDER NODE :
    - to provide the docs
    - check the keys
    - check if patient in chain
    */

    // Keeping the record of the providers in the network
    mapping(address => bool) public Providers;

    // Set user as a provider
    function setProvider(address UserAddress) {
        Providers[_UserAddress] = true;
    }

    // Check if a user address is the provider
    function checkIfProvider(address UserAddress) returns (bool) {
        return Providers[_UserAddress];
    }

    // To check if patients exists
    function patientCheck(uint256 patientWalletAddress)
        public
        view
        returns (bool)
    {}

    // To get the key to the 3rd party
    function getKey(uint256 patientWalletAddress)
        public
        view
        returns (string memory)
    {}

    // Provide the key to the third party to access the docs
    function giveAccessKey(uint256 patientKey)
        public
        view
        returns (string memory)
    {}
}
