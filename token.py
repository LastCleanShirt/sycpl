import string

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

# Operators
OP_ASG = "<Operator Assignment>"

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
SPR             = "!#$%&\'*+,-./:;<=>?@\\^_`|~{}()[]\"\'"
SQR_BRACKETS    = "[]"
CURL_BRACKETS   = "{}"
ROUND_BRACKETS  = "()"
WHITESPACE      = "\t "

# Operator
ASSIGNMENT = "="

def Token(type_=NULL_LTL, val=""):
    return {type_: type_, value: val}
