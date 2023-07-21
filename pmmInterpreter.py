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
        prevclass = ''
        
        for token in line:
            if token[-1] == 'class':
                prevclass = token[0]
                
            if prevclass != '':
                if prevclass == 'console' and token == ['writeln', 'func']:
                    console.writeln('lag')
                
        
    print(Fore.GREEN + 'interpreting finished')