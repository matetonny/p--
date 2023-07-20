from colorama import Fore
from pmmlexer import lexer

def parse(file):
    print(Fore.YELLOW + 'parsing started')
    contents = open(file, 'r').read()
    print(Fore.GREEN + 'parsing finished\n')
    tokens = lexer(contents)
    return tokens