import sys
from colorama import Fore, Style

from client_console_messanger import Client

# if len(sys.argv) != 3:
#     print(Fore.RED + "Incorrect syntax! You should use:")
#     print(Fore.GREEN + "python main.py [ip_address] [port]" + Style.RESET_ALL)
#    exit()

client = Client()

client.start()