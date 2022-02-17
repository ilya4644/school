class Input:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
class TNAnd(Input):
    def dnant(self):
        if self.a == 1 or self.b == 1:
            return 0
        else:
            return 1
class TNOr(Input):
    def ront(self):
        if self.a == 1 and self.b == 1:
            return 0
        else:
            return 1
class TXor(Input):
    def roxt(self):
        return self.a ^ self.b
class TImp(Input):
    def pmit(self):
        if self.a == 1:
            self.a = 0
        else:
            self.a = 1
        if self.a == 1 or self.b == 1:
            return 1
        else:
            return 0
print("Xor")
for i in range(0, 2):
    for j in range(0, 2):
        p = TXor(i, j)
        print(p.roxt())
print("Imp")
for i in range(0, 2):
    for j in range(0, 2):
        p = TImp(i, j)
        print(p.pmit())
