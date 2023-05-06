VAR_DECLR       = "<<VARIABLE DECLARATION>>"
CONST_DECLR     = "<<CONST DECLARATION>>"
OUTPUT          = "<<OUTPUT>>"
INPUT           = "<<INPUT>>"
EXPR            = "<<EXPRESSION>>"

def Instruction(instruction=None, value=""):
    if instruction:
        return {instruction: value}
    else: return
