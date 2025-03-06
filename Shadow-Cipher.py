import argparse
from colorama import init, Fore, Style

init()
SHADOW = Fore.MAGENTA + Style.BRIGHT
VOID = Fore.RED + Style.BRIGHT
TEXT = Fore.WHITE
RESET = Style.RESET_ALL

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_base + shift) % 26 + ascii_base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def print_banner():
    banner = f"""
    {SHADOW}╔════════════════════════════════════╗{RESET}
    {SHADOW}║   Shadow Cipher by Mr. Dr          ║{RESET}
    {SHADOW}║   Forged in the Abyss              ║{RESET}
    {SHADOW}╚════════════════════════════════════╝{RESET}
    """
    print(banner)

def main():
    parser = argparse.ArgumentParser(
        description=f"{SHADOW}A cryptic tool to encode and decode secrets in the shadows.{RESET}",
        epilog=f"{VOID}Beware: The darkness hides what you seek.{RESET}"
    )
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose to encrypt or decrypt")
    parser.add_argument("text", help="The text to process")
    parser.add_argument("-s", "--shift", type=int, default=3, help="Shift value (1-25), default is 3")

    args = parser.parse_args()

    print_banner()

    if args.shift < 1 or args.shift > 25:
        print(f"{VOID}Error: Shift must be between 1 and 25.{RESET}")
        return

    if args.mode == "encrypt":
        result = encrypt(args.text, args.shift)
        print(f"{SHADOW}Encrypted Shadow:{RESET} {TEXT}{result}{RESET}")
    elif args.mode == "decrypt":
        result = decrypt(args.text, args.shift)
        print(f"{SHADOW}Decrypted Truth:{RESET} {TEXT}{result}{RESET}")

if __name__ == "__main__":
    main()
