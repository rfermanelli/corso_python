import lexer
import parser

def compiler(file):
    with open(file) as source_code:
        linea = source_code.readline()
        while linea:
            token = lexer.lexer(linea)
            syntax_tree = parser.parser(token)
            if syntax_tree:
                linea = source_code.readline()
            else:
                return False
        return True

if __name__ == "__main__":
    file = input("Inserisci il nome del file da analizzare completo di esetnsione ---> ")
    if compiler(file):
        pass
    else:
        print("Syntax error")