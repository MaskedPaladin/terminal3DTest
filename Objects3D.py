from Canvas import *

class Object3D:
    def __init__(self):
        self.vectors = []
    def add(self, vector):
        self.vectors.append(vector)
    def delete(self, index):
        self.vectors.pop(index)
    def getVectors(self):
        return self.vectors
class Vector3D:
    def __init__(self, xa, ya, za, xb, yb, zb):
        self.a = [xa, ya, za]
        self.b = [xb, yb, zb]
    def getVector(self):
        return [self.a, self.b]
