// SPDX_License_Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

// To allow higher permissions for event having a custom data type (struct)
pragma experimental ABIEncoderV2;

contract Patient {
    // USER ADDRESS
    address public AddressOfUser;

    constructor() public {
        AddressOfUser = msg.sender;
    }
}
