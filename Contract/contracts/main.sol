// SPDX-License-Identifier: MIT
pragma solidity ^0.5.8;

// To allow higher permissions for event having a custom data type (struct)
pragma experimental ABIEncoderV2;

// Interface for Provider Contract Interaction
interface IProvider {
    function checkIfProvider(address _AddressOfUser)
        external
        payable
        returns (bool);
}

contract Main {
    /// variables ///
    /// @dev Address of the user
    address public AddressOfUser;

    constructor() public {
        AddressOfUser = msg.sender;
    }

    struct AccessKey {
        string Key;
        bool Valid;
    }

    struct PatientsData {
        uint256 id;
        AccessKey PatientKey;
        bool ValidPatient;
    }

    /// @notice EVENTS for Data in blockchain
    event ValidatePatient(uint256 id, bool ValidPatient);
    event InvalidatePatient(uint256 id, bool ValidPatient);
    event PatientAdded(address _PatientAddress, string _PatientKeyGenerated);
    event UserApproved(address _approveTo, address User);

    /// @dev Main Database of the Keys and Patients
    mapping(address => mapping(uint256 => PatientsData)) Patients;
    /// @dev This will keep record of the keys generated by the patient
    mapping(address => uint256) KeysGenerated;
    /// @dev Keeps the mapping of the total approved users to access the key of particular patient address
    mapping(address => uint256) TotalApprovedUsers;
    /// @dev Keeping the track of Approved User Address of the patient
    mapping(address => mapping(uint256 => address)) ApprovedUsers;

    /// @dev To check if the user is a provider is not
    /// @param _AddressOfUser Address of the user
    function checkIfProvider(address _AddressOfUser)
        public
        payable
        returns (bool)
    {
        return
            IProvider(0xAc12C37e47C3cf8ac162Da3f67364f4676825bb3)
                .checkIfProvider(_AddressOfUser);
    }

    /// @dev MODIFIERS for provider functions
    modifier onlyProvider() {
        require(
            checkIfProvider(AddressOfUser) == true,
            "You must be a provider to access this function"
        );
        _;
    }

    /// @dev Check if patient exists in DB
    /// @param _PatientWalletAddress Address of the Patient Wallet
    function checkPatient(address _PatientWalletAddress)
        public
        payable
        onlyProvider
        returns (bool)
    {
        PatientsData memory _patient_data = Patients[_PatientWalletAddress][0];
        if (_patient_data.id == 0) {
            return true;
        } else {
            return false;
        }
    }

    /// @dev Generate key for patient
    /// @param _PatientAddress Address of the Patient
    /// @param _PatientKeyGenerated Generated key of the patient
    function addPatientToDatabase(
        address _PatientAddress,
        string memory _PatientKeyGenerated
    ) public payable onlyProvider {
        uint256 keysCount = KeysGenerated[_PatientAddress];
        PatientsData storage p = Patients[_PatientAddress][keysCount];
        p.id = keysCount;
        p.PatientKey.Key = _PatientKeyGenerated;
        p.PatientKey.Valid = true;
        p.ValidPatient = true;
        KeysGenerated[_PatientAddress]++;
        emit PatientAdded(_PatientAddress, _PatientKeyGenerated);
    }

    /// @dev To approve third party to access the key
    /// @param _approveTo Address of the third party
    function approveUserForKeyAccess(address _approveTo) public payable {
        uint256 totalApproveUsers = TotalApprovedUsers[msg.sender];
        address u = ApprovedUsers[msg.sender][totalApproveUsers];
        u = _approveTo;
        emit UserApproved(_approveTo, msg.sender);
    }

    /// @dev To get the patient key
    /// @param _patientAddress Address of the patient
    function getPatientKey(address _patientAddress)
        public
        view
        returns (PatientsData memory data)
    {
        require(
            _approvalGranted(_patientAddress),
            "You don't have approval for patient data"
        );

        return Patients[_patientAddress][0];
    }

    /// @dev To check if party approved to access address or not
    /// @param _patientAddress Address of the patient
    function _approvalGranted(address _patientAddress)
        private
        view
        returns (bool)
    {
        uint256 totalApproveByPatient = TotalApprovedUsers[_patientAddress];
        for (uint256 i = 0; i < totalApproveByPatient; i++) {
            if (ApprovedUsers[_patientAddress][i] == msg.sender) {
                return true;
            }
        }
        return false;
    }

    /// @dev To get the self keys
    function getSelfKeys() public view returns (PatientsData memory data) {
        return Patients[msg.sender][0];
    }
}
