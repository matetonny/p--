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
        nextTokenIsUsedwrtln = False
        nextTokenIsUsedwrt = False
        notThisTime = False
        
        for token in line:
            if token[-1] == 'class':
                prevclass = token[0]
                
            if prevclass != '':
                if prevclass == 'console' and token == ['writeln', 'func']:
                    nextTokenIsUsedwrtln = True
                    notThisTime = True
                    
                    prevclass = ''
                elif prevclass == 'console' and token == ['write', 'func']:
                    nextTokenIsUsedwrt = True
                    notThisTime = True
                    
                    prevclass = ''
                    
            if nextTokenIsUsedwrtln and token[-1] == 'string' and (notThisTime):
                console.writeln(Fore.WHITE + token[0][1:-1])
                
                nextTokenIsUsedwrtln = False
                
            elif nextTokenIsUsedwrt and token[-1] == 'string' and (notThisTime):
                console.write(Fore.WHITE + token[0][1:-1])
                
                nextTokenIsUsedwrt = False
        
    print(Fore.GREEN + '\ninterpreting finished')