from lexer import Lexer
from parser import Parser

data = "3.14159265359 + (2 / 8) * 9"
lexer = Lexer(data)
parser = Parser(lexer)

result = parser.parse()
print(result)
