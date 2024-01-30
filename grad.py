class Grad:
    def __init__(self, a: float, x: float, n: float=1) -> float:
        self.a = a
        self.x = x
        self.n = n
        
    def grad(self):
        return self.a*(self.n*(self.x**(self.n-1)))

