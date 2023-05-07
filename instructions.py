VAR_DECLR       = "<<VARIABLE DECLARATION>>"
CONST_DECLR     = "<<CONST DECLARATION>>"
OUTPUT          = "<<OUTPUT>>"
INPUT           = "<<INPUT>>"
EXPR            = "<<EXPRESSION>>"

MATHOP          = "<<MATHEMATICAL OPERATION>>"

def Instruction(instruction=None, value=""):
    if instruction:
        return {instruction: value}
    else: return
