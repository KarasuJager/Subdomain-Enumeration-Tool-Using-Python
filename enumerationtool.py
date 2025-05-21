import requests
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SUB ENUM TOOL")
print(ascii_banner)

sub_list = open("wordlist.txt").read() #variable para llamar a la lista podemos cambiar el wordlist.txt por una ruta de archivo con mas words
subs = sub_list.splitlines() #la variable que hemos llamado vamos a que divida la lista por lineas divididas que hara una lista con el wordlist

for sub in subs:
    sub_domain = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domain)
    except requests.ConnectionError:
        pass
    else:
        print("Valid domain :" , sub_domain)