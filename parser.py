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



    # Input and Output
    ## GETOUT
    def _getout(self):
        if self.currentValue() == "getout" and self.currentKey(1) == T.CLN_SPR:
            self._adv(2)
            if self.currentKey() in [T.STR_LTL, T.IDENTIFIER]:
                return Instruction(I.OUTPUT, self.currentValue())
            elif self.currentKey() in [T.FLT_LTL, T.INT_LTL]:
                return Instruction(I.OUTPUT, self._numcalc())
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


    # VARIABLE DECLARATION
    ## Non-Constant
    def _vardeclr(self):
        if self.currentKey() == T.DEC_KWD and self.currentKey(1) == T.IDENTIFIER:
            self._adv(2)
            if self.currentKey() == T.EQ_OP and self.currentKey(1) in [T.STR_LTL, T.IDENTIFIER]:
                return Instruction(I.VAR_DECLR, self.currentValue())
            elif self.currentKey() == T.EQ_OP and self.currentKey(1) in [T.INT_LTL, T.FLT_LTL]:
                self._adv()
                return Instruction(I.VAR_DECLR, self._numcalc())

            else:
                print(SyntaxErr(extra="STRING | INTEGER | FLOAT Expected", loc="-"))
                return None

        else:
            return None

    ## Constant
    def _cdeclr(self):
        if self.currentKey() == T.CDEC_KWD and self.currentKey(1) == T.IDENTIFIER:

            if self.currentKey() == T.EQ_OP and self.currentKey(1) in [T.STR_LTL, T.IDENTIFIER]:
                self._adv()
                return Instruction(I.CONST_DECLR, self.currentValue())
            elif self.currentKey() == T.EQ_OP and self.currentKey(1) in [T.INT_LTL, T.FLT_LTL]:
                self._adv()
                return Instruction(I.CONST_DECLR, self._numcalc())

            else:
                print(SyntaxErr(extra="STRING | INTEGER | FLOAT Expected", loc="-"))
                return None

        else:
            return None

    def _numcalc(self):
        # Working on  shunting yard algorithm
        if self.currentKey() in [T.FLT_LTL, T.INT_LTL]:
            outputq = []
            operators = []

            while self.currentKey() in [T.FLT_LTL, T.INT_LTL, T.PLS_OP, T.MIN_OP, T.MUL_OP, T.DIV_OP]:
                if self.currentKey() in [T.FLT_LTL, T.INT_LTL]:
                    outputq.append(self.currentValue())
                    self._adv()

                elif self.currentKey() in [T.PLS_OP, T.MIN_OP,T.MUL_OP, T.DIV_OP]:
                    if self.currentKey() in [T.PLS_OP, T.MIN_OP]:
                        if len(operators) > 0 and operators[-1] in "*/":
                            outputq.append(operators.pop())
                        operators.append(self.currentValue())
                        self._adv()
                    elif self.currentKey() in [T.MUL_OP, T.MIN_OP]:
                        if len(operators) > 0 and operators[-1] in "*/":
                            outputq.append(operators.pop())
                        operators.append(self.currentValue())
                        self._adv()


            while operators:
                ops = operators.pop()
                outputq.append(ops)

            self._adv(-1)

            return outputq
                
  

    def Parse(self):
        i = []
        while self.ct is not None:
#            print(f"ct: {self.ct}, key: {self.currentKey()}, val: {self.currentValue()}")

            getout  = self._getout()
            getin   = self._getin()
            dec     = self._vardeclr()
            cdec    = self._cdeclr()

            if getout is not None: i.append(getout)
            elif getin is not None: i.append(getin)
            elif dec is not None: i.append(dec)
            elif cdec is not None: i.append(cdec)

            self._adv()

        self.instructions = i
