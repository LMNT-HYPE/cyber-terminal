import os
import random
import time

GREEN = "\033[92m"
DIM = "\033[2m"
RESET = "\033[0m"


def type_out(text, delay=0.025):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(GREEN + DIM + "CYBER TERMINAL // v1.0" + RESET)
    print(GREEN + "=" * 32 + RESET)
    type_out("Booting secure session...", 0.04)
    time.sleep(0.4)

    for step in ["Scanning network", "Decrypting packet", "Opening archive"]:
        type_out(f"[+] {step}" + "." * random.randint(3, 7), 0.03)
        time.sleep(0.35)

    print()
    type_out(GREEN + "ACCESS GRANTED" + RESET, 0.06)
    type_out("You found the secret: KEEP-CODING", 0.04)
    print()
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
