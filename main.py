import os
import json
import secrets
import string
from datetime import datetime

from crypto import (
    xor_encrypt,
    xor_decrypt,
    stream_encrypt,
    stream_decrypt,
    double_encrypt,
    double_decrypt
)

SESSION_FILE = "session.json"

ASCII = r"""
                                             ░██    
                                             ░██    
 ░███████  ░██░████ ░██    ░██ ░████████  ░████████ 
░██    ░██ ░███     ░██    ░██ ░██    ░██    ░██    
░██        ░██      ░██    ░██ ░██    ░██    ░██    
░██    ░██ ░██      ░██   ░███ ░███   ░██    ░██    
 ░███████  ░██       ░█████░██ ░██░█████      ░████ 
                           ░██ ░██                  
                     ░███████  ░██                  by camzzz    https://github.com/cameleonnbss
"""


def clear():
    try:
        os.system(
            "cls" if os.name == "nt"
            else "clear"
        )
    except:
        pass


def safe_input(text=""):
    try:
        return input(text)
    except:
        return ""


def pause():
    safe_input("\npress enter...")


def load_session():
    if not os.path.exists(SESSION_FILE):
        return {
            "last_key": "",
            "last_mode": "stream"
        }

    try:
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "last_key": "",
            "last_mode": "stream"
        }


def save_session(data):
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f, indent=2)


def banner():
    clear()

    print(ASCII)

    print(" local crypter")
    print(
        f" build : {datetime.now().strftime('%Y-%m-%d')}"
    )

    print("-" * 58)


def generate_key(length=32):
    chars = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()-_=+"
    )

    return "".join(
        secrets.choice(chars)
        for _ in range(length)
    )


def encrypt_data(data, key, mode):
    if mode == "1":
        return xor_encrypt(data, key)

    elif mode == "2":
        return stream_encrypt(data, key)

    return double_encrypt(data, key)


def decrypt_data(data, key, mode):
    if mode == "1":
        return xor_decrypt(data, key)

    elif mode == "2":
        return stream_decrypt(data, key)

    return double_decrypt(data, key)


def choose_mode():
    print("\n[1] XOR")
    print("[2] Stream")
    print("[3] Double\n")

    return safe_input("> ").strip()


def encrypt_menu(session):
    banner()

    print("[ encrypt ]\n")

    text = safe_input("text > ")

    print("\n[1] Use saved key")
    print("[2] Enter key")
    print("[3] Generate key\n")

    option = safe_input("> ").strip()

    if option == "1":
        key = session["last_key"]

    elif option == "2":
        key = safe_input(
            "key > "
        ).strip()

    else:
        size = safe_input(
            "length [32] > "
        ).strip()

        if not size.isdigit():
            size = 32
        else:
            size = int(size)

        key = generate_key(size)

        print("\nnew key:\n")
        print(key)

    if not key:
        print("\nno key selected")
        pause()
        return

    mode = choose_mode()

    result = encrypt_data(
        text,
        key,
        mode
    )

    session["last_key"] = key
    session["last_mode"] = mode

    save_session(session)

    banner()

    print("[ encrypted ]\n")
    print(result)

    pause()


def decrypt_menu(session):
    banner()

    print("[ decrypt ]\n")

    data = safe_input("data > ")

    print("\n[1] Use saved key")
    print("[2] Enter key\n")

    option = safe_input("> ").strip()

    if option == "1":
        key = session["last_key"]
    else:
        key = safe_input(
            "key > "
        ).strip()

    if not key:
        print("\nno key selected")
        pause()
        return

    mode = choose_mode()

    try:
        result = decrypt_data(
            data,
            key,
            mode
        )

        banner()

        print("[ decrypted ]\n")
        print(result)

    except:
        print(
            "\ninvalid key or corrupted data"
        )

    pause()


def keygen_menu(session):
    banner()

    print("[ generate key ]\n")

    size = safe_input(
        "length [32] > "
    ).strip()

    if not size.isdigit():
        size = 32
    else:
        size = int(size)

    key = generate_key(size)

    session["last_key"] = key

    save_session(session)

    print("\nnew key:\n")
    print(key)

    pause()


def settings_menu(session):
    banner()

    print("[ settings ]\n")

    print(
        f"saved key  : {session['last_key']}"
    )

    print(
        f"saved mode : {session['last_mode']}"
    )

    print("\n[1] Clear key")
    print("[2] Back\n")

    choice = safe_input("> ").strip()

    if choice == "1":
        session["last_key"] = ""
        save_session(session)

        print("\nkey removed")

        pause()


def main():
    session = load_session()

    while True:
        banner()

        print("[1] Encrypt")
        print("[2] Decrypt")
        print("[3] Generate key")
        print("[4] Settings")
        print("[Q] Exit")

        if session["last_key"]:
            print(
                f"\nactive key : {session['last_key']}"
            )

        print(
            f"mode : {session['last_mode']}"
        )

        choice = safe_input(
            "\n> "
        ).strip().lower()

        if choice == "1":
            encrypt_menu(session)

        elif choice == "2":
            decrypt_menu(session)

        elif choice == "3":
            keygen_menu(session)

        elif choice == "4":
            settings_menu(session)

        elif choice == "q":
            break


if __name__ == "__main__":
    main()
