from colorama import Fore

def listToStr(list):
    result = ''
    for lt in list:
        result += lt
        
    return result

def lexer(contents):
    print(Fore.YELLOW + 'lexing started')
    
    lines = contents.split('\n')
    tokenizedCode = []
    
    
    
    for line in lines:
        
        print(Fore.CYAN + 'line: ' + line)
        
        chars = list(line)
        
        tokens = []
        temp_str = ''
        qoute_count = 0
        index = 0
        
        for char in chars:
            if char == '\'':
                qoute_count += 1
            if qoute_count % 2 == 0:
                in_qoutes = False
            else:
                in_qoutes = True
                
            index += 1
        
        for char in chars:
            if char == '(' or char == '.' or char == '=' or char == '$' or char == ')':
                tokenIsClass = char == '.'
                tokenIsInt = char == '$'
                
                if char == '=':
                    temp_str += '='
                
                if tokenIsClass:
                    tokens.append([temp_str, 'class'])
                    
                elif tokens[-1] == '':
                    if tokens[-2][1] == 'class':
                        tokens.append([temp_str, 'func'])
                elif tokens[-1] != '':
                    if tokens[-1][1] == 'class':
                        tokens.append([temp_str, 'func'])
                    
                if temp_str != '':
                    if temp_str[0] == '\'' and temp_str[-1] == '\'':
                        tokens.append([temp_str, 'string'])
                
                    elif tokenIsInt:
                        tokens.append([temp_str, 'int'])
                        
                if temp_str.isdecimal() and not (temp_str[0] == '\'' and temp_str[-2] == '\''):
                    print('test')
                    
                temp_str = ''
            else:
                temp_str += char
                
            tokenIsClass = char == '.'
        
        tokenizedCode.append(tokens)
        
        
        
    index = 0
    
    for tokens in tokenizedCode:
        index1 = 0
        
        for token in tokens:
            if (not (token[0][0] == '\'' and token[0][-1] == '\'')) and (' ' in token[0]):
                list_token = list(tokenizedCode[index][index1][0])
                list_token.remove(' ')
                tokenizedCode[index][index1][0] = listToStr(list_token)
            
            index1 += 1
            
        index += 1
        
        
    
    while [] in tokenizedCode:
        tokenizedCode.remove([])
    
    print(Fore.CYAN + 'tokenized code: ' + str(tokenizedCode))
    print(Fore.GREEN + 'lexing finished')        
    return tokenizedCode