var contract;
ethereum.enable();
var address="0x3Aa45EBeFd1383Dbee4d408b3117589d44E6C4ef";
var gasPriceval="3";
var gasval="300";
$(document).ready(function(){
	
	web3=new Web3(web3.currentProvider);
	//var address="0x64ADd870Fb9d6DbdA79504a7458CaDDF6CfE74da";
	var abi=[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "data",
				"type": "string"
			}
		],
		"name": "getRecord",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "typeofuser",
				"type": "string"
			}
		],
		"name": "Login",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "key",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "dob",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "mobile",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "email",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "password",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "typeofuser",
						"type": "string"
					}
				],
				"internalType": "struct Fakeproduct.userinfo[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "filename",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pcategory",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pprice",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "username",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "passw",
				"type": "string"
			}
		],
		"name": "addFiledetails",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pcat",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pprice",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "qrname",
				"type": "string"
			}
		],
		"name": "addQrCode",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "allQrInformation",
		"outputs": [
			{
				"internalType": "address",
				"name": "key",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "pid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pcat",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pprice",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "qrname",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "allfiledetailss",
		"outputs": [
			{
				"internalType": "address",
				"name": "key",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "filename",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pcategory",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pprice",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "username",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "passw",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "allusers",
		"outputs": [
			{
				"internalType": "address",
				"name": "key",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dob",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mobile",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "typeofuser",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dob",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mobile",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "typeofuser",
				"type": "string"
			}
		],
		"name": "userRegister",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "typeofuser",
				"type": "string"
			}
		],
		"name": "validateProduct",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "key",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "dob",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "mobile",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "email",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "password",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "typeofuser",
						"type": "string"
					}
				],
				"internalType": "struct Fakeproduct.userinfo[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pcat",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pprice",
				"type": "string"
			}
		],
		"name": "viewQrcode",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "key",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "pid",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pname",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pcat",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pprice",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "qrname",
						"type": "string"
					}
				],
				"internalType": "struct Fakeproduct.qrinformation[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			}
		],
		"name": "viewUploadedproducts",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "key",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "filename",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pid",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pname",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pcategory",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pprice",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "username",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "passw",
						"type": "string"
					}
				],
				"internalType": "struct Fakeproduct.filedetails[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
];
	contract=new web3.eth.Contract(abi,address);
})
