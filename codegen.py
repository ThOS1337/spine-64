registers = {
    "ret": 0,  # rax
    "cnt": 1, 
    "dta": 2,
    "r1": 3,
    "stp": 4,
    "sbp": 5,
    "src": 6,
    "dst": 7,
    "r2": 8,
    "r3": 9,
    "r4": 10,
    "r5": 11,
    "r6": 12,
    "r7": 13,
    "r8": 14,
    "r9": 15
}

class CodeGen:
    def __init__(self):
        self.output = bytearray()
        self.symbols = {}
        self.patches = []
    def mapPass(self, ast):
        # empty
    def emitPass(self, ast):
        # empty
    def patchPass(self):
        # empty
    def outputPass(self, filename):
        # empty