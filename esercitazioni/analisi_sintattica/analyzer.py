from lexer import Lexer
from parser import Parser

with open("sw.txt", "r") as code:
    string = code.readline()
    while string:
        lexer_lsw = Lexer(string)
        token_stream = [lemma for lemma in lexer_lsw.lexer()]
        print(token_stream)
        lexical_error = list(filter(lambda token: token[1] == 'Lexical error', token_stream))
        if not lexical_error:
            pass
            # qui è chiamato il parser
        else:
            print(lexical_error)
        string = code.readline()