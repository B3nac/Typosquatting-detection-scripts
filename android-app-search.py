import requests
import sys

search_list = []

def search():
    arg = sys.argv[1]
    apk_list = []

    search = requests.get('https://play.google.com/store/search?q=' + arg + '&c=apps')
    filter_text = search.text
    for line in filter_text.split():
        if "com." in line:
            line = ''.join(c for c in line if c not in ',[]"<>;/')
            delete_before_equals = line.split('=', 1)[-1]
            delete_before_period = delete_before_equals.split('.', 1)[-1]
            add_com = "com." + delete_before_period
            search_list.append(add_com)
            [apk_list.append(x) for x in search_list if x not in apk_list]
            print(str('\n'.join(apk_list)))

def main():
    search()
main()
