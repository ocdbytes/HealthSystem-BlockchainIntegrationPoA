// SPDX_License_Identifier: UNLICENSED
pragma solidity >=0.6.6 <0.9.0;

contract Provider {
    address public AddressOfProvider;
    address public owner;

    constructor() {
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
    function setProvider(address _UserAddress) private onlyOwner {
        Providers[_UserAddress] = true;
    }

    // Check if a user address is the provider
    function checkIfProvider(address _UserAddress) public view returns (bool) {
        return Providers[_UserAddress];
    }
}
