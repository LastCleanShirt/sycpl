import lexer as lex

class Parser:
    def __init__(self, data):
        self.data = data
        self.lexer = lex.Lexer(self.data)
        self.lexer.Lex()
    def Parse(self):
        return self.lexer.getToken()
