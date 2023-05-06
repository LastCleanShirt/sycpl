class Error:
    def __init__(self, name="DefaultError", loc="", extra="-"):
        self.name   = name
        self.loc    = loc
        self.extra  = extra

    def __repr__(self):
        return f"""{self.name}: {self.extra} at {self.loc}
        """

class SyntaxErr(Error):
    def __init__(self, name="SyntaxError", loc="", extra="-"):
        super().__init__(name, loc, extra)

class InputErr(Error):
    def __init__(self, name="InputError", loc="", extra="-"):
        super().__init__(name, loc, extra)
