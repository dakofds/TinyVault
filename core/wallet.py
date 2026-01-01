from core.seed import *
from bitcoinlib.wallets import Wallet, wallet_exists
from bitcoinlib.keys import HDKey

# --- main functions ---
def new_wallet():
    name = input("Wallet name: ")
    password = input("Password: ")
    print("Wallet type: \n 1 - Bitcoin(mainnet)")
    wtype = input("Type: ")

    if wtype == "1":
        network = 'bitcoin'
    else:
        print("Invalid wallet type")
        return

    print("!!WARNING - Save your seed offline or in a paper - if you dont you'll lose your wallet!! ")
    seed = generate_seed()
    

    wallet = Wallet.create(
        name=name,
        keys=seed,
        password=password,
        network=network
    )
    return wallet

def import_wallet():
    name = input("Wallet name: ")
    seed = input("Your seed: ")
    password = input("Wallet password: ")
    print("Wallet type: \n 1 - Bitcoin(mainnet)")
    wtype = input("Type: ")
    
    if wtype == "1":
        network = 'bitcoin'
    else:
        print("Invalid wallet type")
        return

    if wallet_exists(name):
        print("Wallet with this name already exists!")
        return

    try:
        hdkey = HDKey.from_passphrase(seed)
    except Exception as e:
        print("ERROR: Invalid seed phrase!")
        print(f"Details: {e}")
        return
        
    wallet = Wallet.create(name=name, keys=hdkey, password=password, network=network)

    print(f"Wallet '{name}' imported successfully!")
    return wallet
    
def whelp():
    print("Help xD")
