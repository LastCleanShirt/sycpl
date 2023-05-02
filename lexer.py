import tokens as T
from tokens import Token 
from errors import *

class Lexer(object):
    def __init__(self, data):
        self.data = data + " "
        
        self.pos        = -1
        self.cc         = None
        self.buffer     = ""
        self.qtype      = ""
        self.instr      = 0
        self.bufferstr  = ""
        self.incmt      = 0
        self.tokens     = []
        self.line       = 1
        self.cpl        = 1
        self._adv()

    def _adv(self):
        self.pos += 1
        self.cc = self.data[self.pos] if self.pos < len(self.data) else None
        self.cpl += 1

    def _advL(self):
        self.line   += 1
        self.cpl    =  1

    def Lex(self):
        tokens = []

        # This is where the whole code goes
        # Just be careful though if you dont understand a single thing DO NOT touch it


        while self.cc != None:
            if self.cc in T.WHITESPACE:
                if self.instr == 1:
                   print(f'append {self.cc}')
                   self.bufferstr += self.cc 
                   self._adv()

                else:
                    if self.buffer != "":
                        tokens.append(Token(T.IDENTIFIER, self.buffer))
                    self.buffer = ""
                    self._adv()
            
            elif self.cc in T.CHAR or self.cc in T.INT or self.cc == "_":
                if self.incmt == 1:
                    self._adv()
                elif self.instr == 1:
                    self.bufferstr += self.cc
                    self._adv()

                else:
                    if self.cc in T.CHAR:
                        self.buffer += self.cc

                    elif self.cc in T.INT:
                        self.buffer += self.cc

                    elif self.cc == "_":
                        self.buffer += self.cc




                    self._adv()

            elif self.cc in T.SPR:
                if self.incmt == 1:
                    if self.cc == "\n":
                        self.incmt = 0
                        self._advL()
                    elif self.instr == 1:
                        #print(T.ReturnError(T.STR_ERR, "lol idiot our lexer is not allowed to do that shit on line ", f"{self.line} + {self.cpl}"))

                        #print(SyntaxErr("SyntaxError", "you can't put comment inside of a string, its illegal!1!", f"{self.line}:{self.cpl}"))
                        pass
                    self._adv()
                elif self.cc in T.S_QUOTE:
                    ## String detection mechanism
                    ## Simple logic stuff really
                    if self.instr == 0:
                        self.instr = 1
                        self.qtype = "S"
                        self._adv()

                    elif self.instr == 1 and self.qtype == "S": # Ok end of single quote string
                        self.instr = 0
                        tokens.append(Token(T.STR_LTL, self.bufferstr))
                        self.qtype = ""
                        self._adv()
                        self.bufferstr = ""

                    elif self.instr == 1 and self.qtype == "D": # This time if a there is a double quote character on a single quote string, it will append the double quote string
                        self.bufferstr += self.cc
                        self._adv()

                elif self.cc in T.D_QUOTE:
                    if self.instr == 0:
                        self.instr = 1
                        self.qtype = "D"
                        self._adv()

                    elif self.instr == 1 and self.qtype == "D":
                        self.instr = 0
                        tokens.append(Token(T.STR_LTL, self.bufferstr))
                        self.qtype = ""
                        self._adv()
                        self.bufferstr = ""

                    elif self.instr == 1 and self.qtype == "S": # Same with the line 69 but reversed
                        self.bufferstr += self.cc
                        self._adv()
                else:

                        # COMMENT
                    if self.cc == "$":
                            # IF IT IS INSIDE OF A STRING
                            if self.instr == 1:
                                self.bufferstr = ""
                                print(SyntaxErr("SyntaxError", "you can't put comment inside of a string, its illegal!1!", f"{self.line}:{self.cpl}"))
                                #self._adv()

                                break
                            elif self.incmt == 1:
                                self._adv()
                            elif self.incmt == 0: # Im too lazy to even think about it lol
                                self._adv()

                            self.incmt = 1

                    ## Now THIS IS Separator
                    elif self.cc in "+":
                        self.buffer = ""
                        if self.buffer != "": tokens.append(Token(T.IDENTIFIER, self.buffer))

                        if self.instr == 1:
                            self.bufferstr += self.cc
                        else:
                            tokens.append(Token(T.PLS_ASG, "+"))
                            
                        
                        self._adv()

                    elif self.cc in T.ROUND_BRACKETS:
                        if self.cc == "(": tokens.append(Token(T.RBO_SPR, "("))
                        else: tokens.append(Token(T.RBC_SPR, ")"))

                    elif self.cc in T.CURL_BRACKETS:
                        if self.cc == "{": tokens.append(Token(T.CBO_SPR, "{"))
                        else: tokens.append(Token(T.CBC_SPR, "}"))

                    elif self.cc in T.SQR_BRACKETS:
                        if self.cc == "[": tokens.append(Token(T.SBO_SPR, "["))
                        else:  tokens.append(Token(T.SBC_SPR, "]"))

                    # IND
                    # Ok jadi gua bisa aja pertama pisah2 in if statement nya jadi pilih dlu lagi state comment, string, atau apa gitu, tapi gua males soalnya itu lebih susah menurut gua, menurut gua jg lebih gampang pake mekanisme kayak gini walaupun kalau di debug jadi ribet
                    else:
                        if self.cc in T.EOF:
                            if self.instr == 1:
                                self.bufferstr += self.cc
                            elif self.buffer != "":
                                tokens.append(Token(T.IDENTIFIER, self.buffer))
                                self.buffer = ""
                            self._adv()
                            self._advL()

            elif self.cc in T.INT:
                if self.instr == 1:
                    self.bufferstr += self.cc
                    self._adv()
                



            else:
                self._adv()

        self.tokens = tokens

    def getToken(self):
        return self.tokens
