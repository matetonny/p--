from colorama import Fore

def Interpret(tokenizedCode):
    print(Fore.YELLOW + 'interpreting started\n\n')
    
    class console:
        def __init__(self):
            self.conColor = Fore.WHITE
        
        def writeln(self, string):
            print(self.conColor + string)
        
        def write(self, string):
            print(self.conColor + string, end='')
            
        def chc(self, color):
            self.conColor = color
        
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
                    
                elif prevclass == 'console' and token == ['chcred', 'func']:
                    console.chc(Fore.RED)
                    
                    prevclass = ''
                    
                elif prevclass == 'console' and token == ['chcrblue', 'func']:
                    console.chc(Fore.BLUE)
                    
                    prevclass = ''
                
                elif prevclass == 'console' and token == ['chcyellow', 'func']:
                    console.chc(Fore.YELLOW)
                    
                    prevclass = ''
                    
                elif prevclass == 'console' and token == ['chcwhite', 'func']:
                    console.chc(Fore.WHITE)
                    
                    prevclass = ''
                    
                elif prevclass == 'console' and token == ['chcblack', 'func']:
                    console.chc(Fore.BLACK)
                    
                    prevclass = ''
                    
                elif prevclass == 'console' and token == ['chcgreen', 'func']:
                    console.chc(Fore.GREEN)
                    
                    prevclass = ''
                
                elif prevclass == 'console' and token == ['chcomagenta', 'func']:
                    console.chc(Fore.MAGENTA)
                    
                    prevclass = ''
                    
            if nextTokenIsUsedwrtln and token[-1] == 'string' and (notThisTime):
                console.writeln(token[0][1:-1])
                
                nextTokenIsUsedwrtln = False
                
            elif nextTokenIsUsedwrt and token[-1] == 'string' and (notThisTime):
                console.write(token[0][1:-1])
                
                nextTokenIsUsedwrt = False
            
        
    print(Fore.GREEN + '\n\ninterpreting finished')