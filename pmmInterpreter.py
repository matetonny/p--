from colorama import Fore

def Interpret(tokenizedCode):
    print(Fore.YELLOW + 'interpreting started')
    
    class console:
        def writeln(self, string):
            print(string)
        
        def write(self, string):
            print(string, end='')
            
        def read(self):
            return input()
        
    console = console()
    
    for line in tokenizedCode:
        for token in line:
            pass
        
    print(Fore.GREEN + 'interpreting finished')