import parser as parse
import instructions as I
import re
from errors import *

class Interpreter:
    def __init__(self, data):
        self.parse = parse.Parser(data)
        self.parse.Parse()
        
        self.variables = []

        self.data   = self.parse.getIns()
        self.pos    = -1
        self.ct     = self.data[self.pos]
        self._adv()
    
    # CONST AND VARIABLES
    def add_ncvar(self, name, val=None):
        if not val: return None

        self.variables.append({"type": "variable", "name": name, "value": val})

    def add_cvar(self, name, val=None):
        if not val: return None

        self.variables.append({"type": "const", "name": name, "value": val})

    # INPUT AND OUTPUT
    def output(self, a):
        print(re.sub(r"\\\\", r"\\", a), end="")

    def input(self, a, var):
        pass


    # SC misc.
    def _adv(self, amount=1):
        self.pos += amount
        self.ct = self.data[self.pos] if self.pos < len(self.data) else None

    def currentKey(self, ahead=0):
        return list(self.data[self.pos+ahead].keys())[0]

    def currentValue(self, ahead=0):
        return list(self.data[self.pos+ahead].values())[0]

    def searchVar(self, name):
        for item in self.variables:
            if item["name"] == name:
                return item
        return None

    def Interprete(self):

        while self.ct != None:
            # Output and Input
            if self.currentKey() == I.OUTPUT:
                if isinstance(self.currentKey(), list):
                    pass
                else:
                    self.output(self.currentValue())
                self._adv()

            elif self.currentKey() == I.OUTPUT_VAR:
                var = self.searchVar(self.currentValue())
                if var:
                    self.output(var["value"])
                else:
                    print(NameErr(extra=f"Variable {self.currentValue()} not found"))
                
                self._adv() # TODO: VARIABLE OUTPUT

            elif self.currentKey() in [I.CONST_DECLR, I.VAR_DECLR]:
                if self.currentKey() == I.CONST_DECLR:
                    self.add_cvar(self.currentValue()[0], self.currentValue()[1])
                self._adv()


            
        #return self.parse.getIns()
