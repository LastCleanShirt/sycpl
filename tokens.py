import string

# Tokens
IDENTIFIER = "<Identifier>"

# Keywords
DEC_KWD     = "<variable declaration>"
CDEC_KWD    = "<constant variable declaration>"
GETOUT_KWD  = "<getout keyword>"
GETIN_KWD   = "<getin keyword>"

# Literal
STR_LTL  = "<String Literal>"
INT_LTL  = "<Integer Literal>"
FLT_LTL  = "<Float Literal>"
NULL_LTL = "<Null Literal>"

# Separator
CMT_SPR     = "<Comment Separator>"
SPACE_SPR   = "<Whitespace Separator>"
CLN_SPR     = "<Colon seperator>"

RBO_SPR     = "<Round Brackets Opening>"
RBC_SPR     = "<Round Brackets Closing>"
SBO_SPR     = "<Square Brackets Opening>"
SBC_SPR     = "<Square Brackets Closing>"
CBO_SPR     = "<Curl Brackets Opening>"
CBC_SPR     = "<Curl Brackets Closing>"

# Operators
PLS_OP      = "<Plus operator>"
MIN_OP      = "<Minus operator>"
MUL_OP      = "<Multiply operator>"
DIV_OP      = "<Divide operator>"
EQ_OP       = "<Equal operator>"

OPERATOR_TOKENS = {
    '+': PLS_OP,
    '-': MIN_OP,
    '*': MUL_OP,
    '/': DIV_OP,
}

## Tokens shape
# Keyword
DEC    = "dec"
GETOUT = "getout"
COMEIN = "comein"

# Literal
D_QUOTE   = "\""
S_QUOTE   = "\'"
INT       = "0123456789"
CHAR      = string.ascii_letters

# Separator
SPR             = "!#$%&\'*+,-./:;<=>?@\\^_`|~{}()[]\"\'\n"
SQR_BRACKETS    = "[]"
CURL_BRACKETS   = "{}"
ROUND_BRACKETS  = "()"
WHITESPACE      = "\t "
EOF             = "\n"

# Math
LPAREN          = "("
RPAREN          = ")"
MULTIPLY        = "*"
DIVIDE          = "/"
PLUS            = "+"
MINUS           = "-"


## ERROR TYPES
STR_ERR = "<String Error>"
CMT_ERR = "<Comment Error>"

NT_ERR  = "<NOTYPE Error>"


def Token(type_=NULL_LTL, val=""):
    #return {"type_": type_, "value": val}
    return {type_: val}

## Dear future me, please read this :)
## TODO: Adds feature to change the color of the Error through an extra argument at ReturnError()



