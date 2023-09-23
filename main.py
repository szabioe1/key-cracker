import random
import time
import string
import ctypes
from tqdm import tqdm

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)



def generate_key(length):
    password = ""
    chars = string.ascii_letters + string.digits
    for i in range(length):
        password += random.choice(chars)
    return password

def store_key(num):
    with open('secret.key', "w") as f:
        f.write(generate_key(num))
    print(GREEN + "Key stored! " + RESET)
    time.sleep(2)
    menu()


def store_key_manual(key_string):
    f = open('secret.key', "w")
    f.write(string)
    print(GREEN + "Key stored! " + RESET)
    time.sleep(2)
    menu()

def crack_key():
    with open('secret.key', 'r') as key_read:
        key = key_read.readline()
        chars = string.ascii_letters + string.digits
        secret = ""
        guessed = 0
        wrong = 0

        start_time = time.time()
        with tqdm(total=len(key)) as pbar:
            for char in key:
                while True:
                    randchar = random.choice(chars)
                    if randchar == char:
                        secret += randchar
                        pbar.update(1)
                        #print(GREEN + "Guessed: " + randchar + RESET)
                        time.sleep(0.1)
                        guessed += 1
                        set_console_title(f"Guessed: {guessed} | Wrong: {wrong} | Key: {secret}")
                        break
                    else:
                        #print(RED + "Wrong: " + randchar + RESET)
                        wrong += 1
                        set_console_title(f"Guessed: {guessed} | Wrong: {wrong} | Key: {secret}")
                        continue
        
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Key successfully cracked: {secret}")
        print(f"Time taken to crack: {elapsed_time:.2f} seconds\nIn {guessed} guesses")
        time.sleep(10)


def menu():
    print("Szabioe's cracker")
    menu_choice = input("\n\t1. Store\n\t2. Crack\n")
    if menu_choice == "1":
        key_choice = int(input("\n\t1. Manual key\n\t2. Generated key\n"))
        if key_choice == 1:
            key_input = input("Key: ")
            store_key_manual(key_input)
        elif key_choice == 2:
            key_num = int(input("Length: "))
            store_key(key_num)

    if menu_choice == "2":
        crack_key()


menu()