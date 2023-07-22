
from sys import *
from pmmparser import parse
from pmmInterpreter import Interpret

if __name__ == '__main__':
    Interpret(parse(argv[1]))
    