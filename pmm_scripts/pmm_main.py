#"""
#tokens
#"""

tokenTypes = {
    'INT' : 'int',
    'STR' : 'string',
    'BOOL' : 'bool',
    'FLOAT' : 'float',
    'PLUS' : 'plus',
    'MINUS' :'minus',
    'MULT' : 'mult',
    'DIV' : 'div',
    'LPAR' : 'lpar',
    'RPAR' : 'rpar',
    'UND' : 'undefined'
}

class lexer:
    def __init__(self, code):
        self.inputCode = code
        self.codeLines = code.split('\n')   
        self.tokenizedcode = [] 
        
    def proccessTokenType(self, token):
        return 'UND'
    
    def tokenize(self):
        for line in self.codeLines:
            curToken = ''
            
            for lt in line:
                if lt == '+':
                    self.tokenizedcode.append([curToken, tokenTypes[self.proccessTokenType(curToken)]])
                    curToken = ''
                    self.tokenizedcode.append([curToken, tokenTypes['PLUS']])
                elif lt == '-':
                    self.tokenizedcode.append([curToken, tokenTypes[self.proccessTokenType(curToken)]])
                    curToken = ''
                    self.tokenizedcode.append([curToken, tokenTypes['PLUS']])
                elif lt == '*':
                    self.tokenizedcode.append([curToken, tokenTypes[self.proccessTokenType(curToken)]])
                    curToken = ''
                    self.tokenizedcode.append([curToken, tokenTypes['PLUS']])
                elif lt == '/':
                    self.tokenizedcode.append([curToken, tokenTypes[self.proccessTokenType(curToken)]])
                    curToken = ''
                    self.tokenizedcode.append([curToken, tokenTypes['PLUS']])
                elif lt == '(':
                    self.tokenizedcode.append([curToken, tokenTypes[self.proccessTokenType(curToken)]])
                    curToken = ''
                    self.tokenizedcode.append([curToken, tokenTypes['LPAR']])
                elif lt == ')':
                    self.tokenizedcode.append([curToken, tokenTypes[self.proccessTokenType(curToken)]])
                    curToken = ''
                    self.tokenizedcode.append([curToken, tokenTypes['RPAR']])
                    
                else:
                    curToken += lt
                
            print('\n')
            
        print(self.tokenizedcode)