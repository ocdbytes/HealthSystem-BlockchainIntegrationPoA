// SPDX-License-Identifier: MIT
pragma solidity ^0.5.8;

contract Provider {
    address public AddressOfProvider;
    address public owner;

    constructor() public {
        AddressOfProvider = msg.sender;
        owner = msg.sender;
    }

    // Keeping the record of the providers in the network
    mapping(address => bool) public Providers;

    modifier onlyOwner() {
        require(
            msg.sender == owner,
            "you need to be a contract owner in order to execute this function"
        );
        _;
    }

    // Set user as a provider
    function setProvider(address _UserAddress) public onlyOwner {
        Providers[_UserAddress] = true;
    }

    // Check if a user address is the provider
    function checkIfProvider(address _UserAddress) public view returns (bool) {
        return Providers[_UserAddress];
    }
}
