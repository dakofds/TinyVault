from bitcoinlib.mnemonic import Mnemonic

def generate_seed():
    passphrase = Mnemonic().generate()
    return passphrase

def get_seed(wallet, password=None):
    try:
        return wallet.key().mnemonic(password=password)
    except Exception as e:
        return None
