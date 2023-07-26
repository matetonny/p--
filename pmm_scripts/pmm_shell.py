from pmm_main import lexer

lineInput = ''
lexer = lexer('')

while lineInput != 'exit':
    lineInput = input('pmmShell > ')
    
    lexer.codeLines = [lineInput]
    
    lexer.tokenize()