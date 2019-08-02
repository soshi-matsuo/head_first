class CountFromBy:
    
    def __init__(self, v=0, i=1):
        self.val = v
        self.incr = i

    def __repr__(self):
        return str(self.val)

    def increase(self):
        self.val += self.incr