import string
from colorama import Fore, Back, Style

# Tokens
IDENTIFIER = "<Identifier>"

# Keywords
DEC_KWD    = "<decl keyword>"
GETOUT_KWD = "<getout keyword>"
COMEIN_KWD = "<comein keyword>"

# Literal
STR_LTL  = "<String Literal>"
INT_LTL  = "<Integer Literal>"
FLT_LTL  = "<Float Literal>"
NULL_LTL = "<Null Literal>"

# Separator
CMT_SPR     = "<Comment Separator>"
SPACE_SPR   = "<Whitespace Separator>"

RBO_SPR     = "<Round Brackets Opening>"
RBC_SPR     = "<Round Brackets Closing>"
SBO_SPR     = "<Square Brackets Opening>"
SBC_SPR     = "<Square Brackets Closing>"
CBO_SPR     = "<Curl Brackets Opening>"
CBC_SPR     = "<Curl Brackets Closing>"

# Operators
OP_ASG      = "<Operator Assignment>"
PLS_ASG     = "<Plus Assignment>"

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

## ERROR TYPES
STR_ERR = "<String Error>"
CMT_ERR = "<Comment Error>"

NT_ERR  = "<NOTYPE Error>"

## SYS
RESET   = Style.RESET_ALL

def Token(type_=NULL_LTL, val=""):
    #return {"type_": type_, "value": val}
    return {type_: val}

## Dear future me, please read this :)
## TODO: Adds feature to change the color of the Error through an extra argument at ReturnError()



