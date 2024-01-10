
#import pywallet
from hdwallet import HDWallet
from hdwallet.symbols import LTC as SYMBOL
from hdwallet.utils import generate_entropy
from hdwallet.utils import is_entropy
from blockcypher import get_address_overview
from typing import Optional
import json
import os
import requests
import time

def create_ltc_wallet():
    STRENGTH: int = 160  # Default is 128
    # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
    LANGUAGE: str = "english"  # Default is english
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    PASSPHRASE: Optional[str] = None  # "meherett" # Secret passphrase for mnemonic

    # Initialize USDT HDWallet
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)

    # Get USDT HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY,
        language=LANGUAGE,
        passphrase=PASSPHRASE
    )

    # Derivation from path
    # hdwallet.from_path("m/44'/2001'/0'/0/0")  # You can derive from a specific path

    # Or derivation from index
    hdwallet.from_index(44, hardened=True)
    hdwallet.from_index(2001, hardened=True)  # 2001 is the coin type for USDT
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0)
    hdwallet.from_index(0)

    # Print all USDT HDWallet information's
    print("Initializing wallet create procedure...")
    time.sleep(3)
    get_hd = hdwallet.dumps()
    get_hd_crypt = get_hd['cryptocurrency']
    get_hd_addr = get_hd['addresses']

    print(f"""
    Network: {get_hd['network']}
    Wallet type: {get_hd_crypt}\n 
    Wallet Addresses: 
        -p2pkh addr: {get_hd_addr['p2pkh']}
        -p2sh addr: {get_hd_addr['p2sh']}
        -p2wsh addr: {get_hd_addr['p2wsh']}
        -p2wpkh addr: {get_hd_addr['p2wpkh']}
        -p2wpkh_in_p2sh addr: {get_hd_addr['p2wpkh_in_p2sh']}
        -p2wsh_in_p2sh addr: {get_hd_addr['p2wsh_in_p2sh']}
    """)
    #print(json.dumps(get_hd, indent=4, ensure_ascii=False))

    """
    __pass__ = wallet.generate_mnemonic()
    gen_wallet = wallet.create_wallet(network="USDT", seed=__pass__, children=1)  # initialize the passkey to create the wallet
    print(gen_wallet)"""

    details_to_store = {
        'entropy': get_hd['entropy'],
        'addresses': get_hd_addr,
        'seed': get_hd['seed'],
        'mnemonic': get_hd['mnemonic'],
        'public_key': get_hd['public_key'],
        'private_key': get_hd['private_key'],
        'hash': get_hd['hash']
    }

    # Store the details in a JSON file
    with open('wallet_details.json', 'w') as f:
        json.dump(details_to_store, f)


# noinspection PyStatementEffect
def view_balance():
    choice = input('load wallet address automatically(y)/input address manually(n): ')
    if choice == 'y':
        with open('wallet_details.json', 'r') as f:
            data = json.load(f)

        balance_details = get_address_overview(data['addresses']['p2pkh'], coin_symbol="ltc")
        balance_satoshis = balance_details['balance']
        # Convert the balance to LTC (1 LTC is 100 million satoshis)
        balance_ltc = balance_satoshis / 1e8

        print("Fetching balance from blockchain...")
        time.sleep(2)
        print(f"Your balance is: {balance_ltc} ltc")
    elif choice == 'n':
        address = input("Enter ltc wallet address: ")
        bs = get_address_overview(address, coin_symbol='ltc')
        balance_satoshis = bs['balance']
        b_ltc = balance_satoshis / 1e8

        print("Fetching balance from blockchain...")
        time.sleep(2)
        print(f"Your balance is: {b_ltc} ltc")

def load_ltc_wallet():
    decide = input("Load wallet automatically(y)/Enter seed manually(n): ")
    time.sleep(1)
    if decide == 'n':
        seed_in = input("Enter your entropy here: ")

        SEED: str = seed_in
        LANGUAGE: str = "english"  # The language used for the mnemonic
        PASSPHRASE: Optional[str] = None  # The passphrase used for the mnemonic, if any

        # Initialize LTC HDWallet
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)

        # Get LTC HDWallet from seed or mnemonic
        hdwallet.from_entropy(
            entropy=SEED,
            language=LANGUAGE,
            passphrase=PASSPHRASE
        )

        # Derivation from path
        # hdwallet.from_path("m/44'/2001'/0'/0/0")  # You can derive from a specific path

        # Or derivation from index
        hdwallet.from_index(44, hardened=True)
        hdwallet.from_index(2001, hardened=True)  # 2001 is the coin type for LTC
        hdwallet.from_index(0, hardened=True)
        hdwallet.from_index(0)
        hdwallet.from_index(0)

        # Print all LTC HDWallet information's
        print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
        get_hd = hdwallet.dumps()
        get_hd_crypt = get_hd['cryptocurrency']
        get_hd_addr = get_hd['addresses']

        # Print all LTC HDWallet information's
        print('Important details: ')
        time.sleep(3)
        print(f"""
                        Network: {get_hd['network']}
                        Wallet type: {get_hd_crypt}\n 
                        Wallet Addresses: 
                            -p2pkh addr: {get_hd_addr['p2pkh']}
                            -p2sh addr: {get_hd_addr['p2sh']}
                            -p2wsh addr: {get_hd_addr['p2wsh']}
                            -p2wpkh addr: {get_hd_addr['p2wpkh']}
                            -p2wpkh_in_p2sh addr: {get_hd_addr['p2wpkh_in_p2sh']}
                            -p2wsh_in_p2sh addr: {get_hd_addr['p2wsh_in_p2sh']}
                        """)
    elif decide == 'y':
        print('scanning seed..')
        time.sleep(3)
        with open('wallet_details.json', 'r') as f:
            data = json.load(f)

        SEED: str = data['entropy']  # Replace with your actual seed
        LANGUAGE: str = "english"  # The language used for the mnemonic
        PASSPHRASE: Optional[str] = None  # The passphrase used for the mnemonic, if any

        # Initialize LTC HDWallet
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)

        # Get LTC HDWallet from seed or mnemonic
        hdwallet.from_entropy(
            entropy=SEED,
            language=LANGUAGE,
            passphrase=PASSPHRASE
        )

        # Derivation from path
        # hdwallet.from_path("m/44'/2001'/0'/0/0")  # You can derive from a specific path

        # Or derivation from index
        hdwallet.from_index(44, hardened=True)
        hdwallet.from_index(2001, hardened=True)  # 2001 is the coin type for LTC
        hdwallet.from_index(0, hardened=True)
        hdwallet.from_index(0)
        hdwallet.from_index(0)

        # Print all LTC HDWallet information's
        print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
        get_hd = hdwallet.dumps()
        get_hd_crypt = get_hd['cryptocurrency']
        get_hd_addr = get_hd['addresses']

        # Print all LTC HDWallet information's
        print('Important details: ')
        time.sleep(3)
        print(f"""
                Network: {get_hd['network']}
                Wallet type: {get_hd_crypt}\n 
                Wallet Addresses: 
                    -p2pkh addr: {get_hd_addr['p2pkh']}
                    -p2sh addr: {get_hd_addr['p2sh']}
                    -p2wsh addr: {get_hd_addr['p2wsh']}
                    -p2wpkh addr: {get_hd_addr['p2wpkh']}
                    -p2wpkh_in_p2sh addr: {get_hd_addr['p2wpkh_in_p2sh']}
                    -p2wsh_in_p2sh addr: {get_hd_addr['p2wsh_in_p2sh']}
                """)
    else:
        print('Enter a proper load command.')

action = input('What py-usdtwallet action do you want to perform?: ')
if action == 'create':
    create_ltc_wallet()
elif action == 'see_balance':
    view_balance()
elif action == 'load':
    load_ltc_wallet()
else:
    print("Choose a valid action.")