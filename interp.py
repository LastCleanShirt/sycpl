import parser as parse
import instructions as I

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
        print(a, end="")

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

    def Interprete(self):

        while self.ct != None:
            # Output and Input
            if self.currentKey() == I.OUTPUT:
                if isinstance(self.currentKey(), list):
                    pass
                else:
                    self.output(self.currentValue())
            self._adv()
            
        #return self.parse.getIns()
