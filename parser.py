import lexer as lex
import instructions as I
import tokens as T
from instructions import Instruction
from errors import Error, SyntaxErr

class Parser:
    def __init__(self, data):
        self.lexer = lex.Lexer(data)
        self.lexer.Lex()

        self.data = self.lexer.getToken()
        self.data.append({"END": "END"})

        self.instructions = []
        self.pos = -1
        self.ct = self.data[self.pos]

        self.tokens = {
            "GETIN_KWD": T.GETIN_KWD,
            "CLN_SPR": T.CLN_SPR,
            "STR_LTL": T.STR_LTL,
            "IDENTIFIER": T.IDENTIFIER
        }

        self._adv()

    def _adv(self, amount=1):
        self.pos += amount
        self.ct = self.data[self.pos] if self.pos < len(self.data) else None

    def getIns(self):
        return self.instructions

    def currentKey(self, ahead=0):
        return list(self.data[self.pos+ahead].keys())[0]

    def currentValue(self, ahead=0):
        return list(self.data[self.pos+ahead].values())[0]




    ## GEOUT
    def _getout(self):
        if self.currentValue() == "getout" and self.currentKey(1) == T.CLN_SPR:
            self._adv(2)
            if self.currentKey() in [T.STR_LTL, T.INT_LTL, T.FLT_LTL]:
                return Instruction(I.OUTPUT, self.currentValue())
            else:
                print(SyntaxErr(extra="STRING | INTEGER | FLOAT Expected", loc="-"))
                return None
        else:
            return None

    ## GETIN
    def _getin(self): 
    ## THIS IS THE MARKED LINE/FUNCTION
        
        if self.currentValue() == "getin" and self.currentKey(1) == T.CLN_SPR:
            self._adv(2)
            if self.currentKey() == T.STR_LTL and self.currentKey(1) == T.CLN_SPR:
                self._adv(2)
                if self.currentKey() == T.IDENTIFIER:
                    return Instruction(I.INPUT, [self.currentValue(-2), self.currentValue()])
                elif self.currentKey() in [T.INT_LTL, T.FLT_LTL, T.STR_LTL]:
                    print(SyntaxErr(extra="VARIABLE Expected"))
            else:
                print(SyntaxErr(extra="STRING Expected", loc="-"))
                return None
        else:
            return None


    def Parse(self):
        i = []
        while self.ct is not None:
            print(f"ct: {self.ct}, key: {self.currentKey()}, val: {self.currentValue()}")

            getout  = self._getout()
            getin   = self._getin()

            if getout is not None: i.append(getout)
            elif getin is not None: i.append(getin)
            self._adv()

        self.instructions = i
