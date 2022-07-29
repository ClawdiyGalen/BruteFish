from colorama import Fore, Back, Style
import time

i = 0
banner = """
  ____                   _            ______   _         _     
 |  _ \                 | |          |  ____| (_)       | |    
 | |_) |  _ __   _   _  | |_    ___  | |__     _   ___  | |__  
 |  _ <  | '__| | | | | | __|  / _ \ |  __|   | | / __| | '_ \ 
 | |_) | | |    | |_| | | |_  |  __/ | |      | | \__ \ | | | |
 |____/  |_|     \__,_|  \__|  \___| |_|      |_| |___/ |_| |_|


    coded by: ClawdiyGalen

"""
print(Fore.RED + banner)
print(Fore.CYAN + "Брутфорс:\n \n[1]Instagram\n[2]Vk\n")
choice = input(Fore.GREEN + ">>")

if choice == "1":
    input(Fore.YELLOW + "Ссылка на страницу или id >>")

if choice == "2":
    input(Fore.Yellow + "Ссылка на страницу или id >>")

print("\n Брутфорс может занять некоторое время")


while True:
    i += 1
    time.sleep(0.5)
    print(f"Паролей подобрано {i}")
