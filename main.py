import requests
from bs4 import BeautifulSoup
import time
from colorama import init, Fore
import itertools

init(autoreset=True)

def check_status(username):
    url = f"https://guns.lol/{username}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if "This user is not claimed" in soup.text:
            return "Available"
        else:
            return "Taken"
    except requests.RequestException as e:
        print(f"Error during the request for {url}: {e}")
        return None

def print_colored_and_save(status, username):
    if status == "Available":
        print(f"{Fore.GREEN}https://guns.lol/{username} : {status}")
        with open("text.txt", "a") as f:
            f.write(f"https://guns.lol/{username} : {status}\n")
    else:
        print(f"{Fore.RED}https://guns.lol/{username} : {status}")  

def generate_usernames():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    min_len = 3
    max_len = 8
    request_count = 0 

    for length in range(min_len, max_len + 1):
        for comb in itertools.product(letters, repeat=length):
            username = ''.join(comb)

            if request_count > 50:
                print("Too many requests, please wait 1 minute...")
                time.sleep(60)
                request_count = 0 

            status = check_status(username)

            if status:
                print_colored_and_save(status, username)

            time.sleep(0.2)

            request_count += 1

generate_usernames()
