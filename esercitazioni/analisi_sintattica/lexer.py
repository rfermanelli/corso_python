from grammar import TerminalsLsw, Productions

class Lexer:
    def __init__(self, string):
        self.string = string


    def lexicon(self):
        self.string = self.string.upper()
        terminals = self.string.split()
        return terminals


    def terminals(self):
        for terminal in self.lexicon():
            yield terminal, terminal in TerminalsLsw.terminals


    def lexer(self):
        syntax = Productions()
        get_nonterminal = lambda terminal: next((nonterminal for nonterminal, terminals in syntax.syntax.items() if terminal in terminals), None)
        for terminal in self.terminals():
            if terminal[1]:
                nonterminal = get_nonterminal(terminal[0])
                yield terminal[0].upper(), nonterminal.upper()
            else:
                yield terminal[0].upper(), "Lexical error"