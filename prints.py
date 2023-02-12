import colorama
from colorama import Fore
import os
import sys

# Função responsável pela print inicial do menu
def menu():
    os.system('clear')
    print(f"{Fore.BLUE}  _____             _______             _             ")
    print(" |  __ \           |__   __|           | |            ")
    print(" | |__) |__ _  ___ ___| |_ __ __ _  ___| | _____ _ __ ")
    print(" |  _  // _` |/ __/ _ \ | '__/ _` |/ __| |/ / _ \ '__|")
    print(" | | \ \ (_| | (_|  __/ | | | (_| | (__|   <  __/ |   ")
    print(" |_|  \_\__,_|\___\___|_|_|  \__,_|\___|_|\_\___|_|   ")
    print("   _____                          _____ ______         ")
    print("  / ____|                        | ____|____  |       ")
    print(" | |  __ _ __ _   _ _ __   ___   | |__     / /        ")
    print(" | | |_ | '__| | | | '_ \ / _ \  |___ \   / /         ")
    print(" | |__| | |  | |_| | |_) | (_) |  ___) | / /          ")
    print("  \_____|_|   \__,_| .__/ \___/  |____/ /_/           ")
    print("                   | |                                ")
    print("                   |_|                                ")
    print("                                                      ")
    print(f"{Fore.BLACK}                 BEM-VINDO                            ")
    print(f"{Fore.WHITE}                                                     ")
    
    
# Função responsável por printar para o file 
def printar_file(linha):
    original_stdout = sys.stdout
    with open('mapa.txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(linha)
        sys.stdout = original_stdout # Reset the standard output to its original value



# Função que printa o mapa para o terminal -> nao esta a ser usada
def print_matrix():
    file = open('mapa.txt') 
    print(file.read())


def print_bfs():
    print("  ___   _                      _  _                      ______ ______  _____ ")
    print(" / _ \ | |                    (_)| |                     | ___ \|  ___|/  ___|")
    print("/ /_\ \| |  __ _   ___   _ __  _ | |_  _ __ ___    ___   | |_/ /| |_   \ `--. ")
    print("|  _  || | / _` | / _ \ | '__|| || __|| '_ ` _ \  / _ \  | ___ \|  _|   `--. \ ")
    print("| | | || || (_| || (_) || |   | || |_ | | | | | || (_) | | |_/ /| |    /\__/ /")
    print("\_| |_/|_| \__, | \___/ |_|   |_| \__||_| |_| |_| \___/  \____/ \_|    \____/ ")
    print("            __/ |                                                             ")
    print("           |___/                                                              ")

def print_dfs():
    print("  ___   _                      _  _                      ______ ______  _____ ")
    print(" / _ \ | |                    (_)| |                     |  _  \|  ___|/  ___|")
    print("/ /_\ \| |  __ _   ___   _ __  _ | |_  _ __ ___    ___   | | | || |_   \ `--. ")
    print("|  _  || | / _` | / _ \ | '__|| || __|| '_ ` _ \  / _ \  | | | ||  _|   `--. \ ")
    print("| | | || || (_| || (_) || |   | || |_ | | | | | || (_) | | |/ / | |    /\__/ /")
    print("\_| |_/|_| \__, | \___/ |_|   |_| \__||_| |_| |_| \___/  |___/  \_|    \____/ ")
    print("            __/ |                                                             ")
    print("           |___/                                                              ")

def print_astar():
    print("  ___   _                      _  _                              _____  _                ")
    print(" / _ \ | |                    (_)| |                            /  ___|| |               ")
    print("/ /_\ \| |  __ _   ___   _ __  _ | |_  _ __ ___    ___     __ _ \ `--. | |_   __ _  _ __ ")
    print("|  _  || | / _` | / _ \ | '__|| || __|| '_ ` _ \  / _ \   / _` | `--. \| __| / _` || '__|")
    print("| | | || || (_| || (_) || |   | || |_ | | | | | || (_) | | (_| |/\__/ /| |_ | (_| || |   ")
    print("\_| |_/|_| \__, | \___/ |_|   |_| \__||_| |_| |_| \___/   \__,_|\____/  \__| \__,_||_|   ")
    print("            __/ |                                                                        ")
    print("           |___/                                                                         ")

def print_greedy():
    print("  ___   _                      _  _                       _____                        _        ")
    print(" / _ \ | |                    (_)| |                     |  __ \                      | |       ")
    print("/ /_\ \| |  __ _   ___   _ __  _ | |_  _ __ ___    ___   | |  \/ _ __   ___   ___   __| | _   _ ")
    print("|  _  || | / _` | / _ \ | '__|| || __|| '_ ` _ \  / _ \  | | __ | '__| / _ \ / _ \ / _` || | | |")
    print("| | | || || (_| || (_) || |   | || |_ | | | | | || (_) | | |_\ \| |   |  __/|  __/| (_| || |_| |")
    print("\_| |_/|_| \__, | \___/ |_|   |_| \__||_| |_| |_| \___/   \____/|_|    \___| \___| \__,_| \__, |")
    print("            __/ |                                                                          __/ |")
    print("           |___/                                                                          |___/ ")