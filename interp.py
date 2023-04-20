import parser as parse

class Interpreter:
    def __init__(self, data):
        self.data = data
        self.parse = parse.Parser(data)
    def Interprete(self):
        return self.parse.Parse()
