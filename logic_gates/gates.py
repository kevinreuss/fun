class GATE:
    def __init__(self):
        self.a = False
        self.b = False
    def set_a(self, a):
        self.a = a
    def set_b(self, b):
        self.b = b

class AND(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return self.a and self.b

class OR(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return self.a or self.b

class XOR(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return self.a != self.b

class NAND(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return not (self.a and self.b)

class NOR(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return (not self.a) and (not self.b)

class XNOR(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return self.a == self.b

class NOT(GATE):
    def __init__(self):
        super().__init__()
    def get_out(self):
        return not self.a