import token as T

class Lexer(object):
    def __init__(self, data):
        self.data = data
        
        self.pos = -1
        self.cc = None
        self._adv()
        self.buffer = ""

        self.tokens = []

    def _adv(self):
        self.pos += 1
        self.cc = self.data[self.pos] if self.pos < len(self.data) else None

    def Lex(self):
        tokens = []

        # This is where the whole code goes
        # Just be careful though if you dont understand a single thing DO NOT touch it

        while self.cc != None:
            if self.cc in T.WHITESPACE:
                self._adv()
                if self.buffer != "":
                    tokens.append(self.buffer)
                self.buffer = ""
            
            elif self.cc in T.CHAR or self.cc in T.INT or self.cc == "_":
                if self.cc in T.CHAR:
                    self.buffer += self.cc

                elif self.cc in T.INT:
                    self.buffer += self.cc

                elif self.cc == "_":
                    self.buffer += self.cc

                self._adv()

            elif self.cc in T.SPR:
                self._adv()


            else:
                self._adv()
            print(self.tokens)

        self.tokens = tokens

    def getToken(self):
        return self.tokens
