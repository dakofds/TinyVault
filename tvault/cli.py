from core.seed import *
from core.wallet import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Use: tvault help")
        return

    cmd = sys.argv[1].lower()

    if cmd == "new":
        new_wallet()
    elif cmd == "import":
        import_wallet()
    elif cmd == "help":
        whelp()
    else:
        print("Invalid command. Type 'help' for options.")

if __name__=="__main__":
    main()

