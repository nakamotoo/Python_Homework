#問2 複素クラスの四則演算インスタンスメソッド
class Comp:
    def __init__(self, real, imag, ):
        self.real = real
        self.imag = imag
    def add(self, other):
        return Comp(
            self.real + other.real,
            self.imag + other.imag
            )
    def sub(self, other):
        return Comp(
            self.real - other.real,
            self.imag - other.imag
            )
    def mul(self, other):
        return Comp(
            self.real*other.real - self.imag*other.imag,
            self.real*other.imag + self.imag*other.real
            )
    def div(self, other):
        return Comp(
            (self.real*other.real + self.imag*other.imag) / (other.real**2 + other.imag**2),
            (-self.real*other.imag + self.imag*other.real) / (other.real**2 + other.imag**2)
        )
    def to_s(self):
        if self.imag > 0:
            return str(self.real) + " + "  + str(self.imag)+ "i"
        elif self.imag == 0:
            return str(self.real)
        else:
            return str(self.real) + str(self.imag)+ "i"

x = Comp(1, 1) # 1+i
y = Comp(1, -1) # 1-i

a = x.add(y)
b = x.sub(y)
c = x.mul(y)
d = x.div(y)

def test():
    print(a.to_s() == "2")
    print(b.to_s() == "0 + 2i")
    print(c.to_s() == "2")
    print(d.to_s() == "0.0 + 1.0i")

test()
