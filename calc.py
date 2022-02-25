class Calc:
    def __init__(self, a,b):
        self.a = a
        self.b = b
                                
    def main(self):
        return  (self.a + self.b)
    
    def calc_diff(self):
        return (self.a + (-self.b))
    
    def calc_mult(self):
        return (self.a * self.b)
    
    def calc_div(self):
        return (self.a / self.b)
        
a = Calc(4,3)
print(a.calc_div())

print(Calc(4,5).calc_mult())
