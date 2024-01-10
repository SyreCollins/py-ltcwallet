# py-ltcwallet - Python Litecoin Wallet

## Overview
This project provides a set of Python scripts to create, load, and check the balance of a Litecoin (LTC) wallet. It leverages the `hdwallet` and `blockcypher` libraries to interact with the Litecoin blockchain.

## Features
- **Create a new Litecoin wallet**: Generate a new wallet with a unique seed and store the wallet details in a JSON file.
- **Load an existing Litecoin wallet**: Load a wallet using a seed either manually or from a JSON file.
- **Check wallet balance**: View the balance of a Litecoin wallet either by loading the wallet address automatically from a JSON file or by manually entering the address.

## USAGE & COMMANDS
- **create**: Command for creating a new litecoin wallet
- **load**: Command for loading existing wallet from the json file where most details are stored or by inputing the entropy seed manually
- **see_balance**: Command for seeing available litecoin balance.
- 
## FUTURES
 - **I plan to implement a script that allows a user to send litecoin crypto to other litecoin wallets/users.**
 - **I plan to implement a tracker to be able to track crypto transactions.**
   
 **NB;** when creating a new wallet details are stored in a json file and if that same json file already exists, the new create would overwrite all data that might be in the already existed similar json file. So take proper precautions when doing a new create to avoid loss of funds as this can not be regained... THANK YOU!!
 
## Installation
To install the necessary dependencies, run the following command:

```bash
pip install hdwallet
pip install blockcypher
pip install 'any other module' 
