import numpy as np

class Random:

    SEED = 123456789

    def __init__(self) -> None:
        self.modulus = 2147483647      
        self.multiplier = 48271
    
    def getNumber(self):
        Q = np.longlong(self.modulus / self.multiplier)
        R = np.longlong(self.modulus % self.multiplier)

        t = self.multiplier * (self.SEED % Q) - R * (self.SEED / Q)

        if t > 0:
            self.SEED = t
        else:
            self.SEED = t + self.modulus
        
        
        return np.double(self.SEED) / self.modulus
