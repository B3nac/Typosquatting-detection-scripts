import requests
import sys
import urllib.parse
import pip

typo_list = []

def populate_typos():
    with open(str(sys.argv[1])) as f:
        for line in f:
            typo_list.append(str(line))
    f.close()

def send_requests():
    for line in typo_list:
        print("-----------------------------")
        print("Word is: " + line)
        result = pip.main(['search', line])
        print("-----------------------------")
        print(result)

def main():
    populate_typos()
    send_requests()
main()
