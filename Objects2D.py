from Canvas import *

class Object2D:
    def __init__(self):
        self.vectors = []
    def add(self, vector):
        self.vectors.append(vector)
    def delete(self, index):
        self.vectors.pop(index)
    def getVectors(self):
        return self.vectors
class Triangle(Object2D):
    def __init__(self, tscale):
        super().__init__()
        self.add(Vector2D(0,2*tscale,2*tscale,2*tscale))
        self.add(Vector2D(0,2*tscale,1*tscale,1*tscale))
        self.add(Vector2D(1*tscale,1*tscale,2*tscale,2*tscale))
class Square(Object2D):
    def __init__(self, sscale):
        super().__init__()
        self.add(Vector2D(1*sscale, 1*sscale, 2*sscale, 1*sscale))
        self.add(Vector2D(1*sscale, 1*sscale, 1*sscale, 2*sscale))
        self.add(Vector2D(1*sscale, 2*sscale, 2*sscale, 2*sscale))
        self.add(Vector2D(2*sscale, 1*sscale, 2*sscale, 2*sscale))
class Vector2D:
    def __init__(self, xa, ya, xb, yb):
        self.a = [xa, ya]
        self.b = [xb, yb]
    def getVector(self):
        return [self.a, self.b]
    def getDirection(self):
        return [self.b[0] - self.a[0], self.b[1] - self.a[1]]
