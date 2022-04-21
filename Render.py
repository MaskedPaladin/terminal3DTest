from Canvas import *
from Objects2D import *
from Objects3D import *
from MatrixOperations import *
import time
canvas = Canvas(50, 50)

def put2DObjsIntoCanvas(canvas, objs):
    for e in objs:
        for o in e.getVectors():
            v = o.getVector()
            canvas.putLine(v[0][0], v[0][1], v[1][0], v[1][1], "\033[0;0;42m ")
def cube(size):
    obj3d = Object3D()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for g in range(2):
                    for h in range(2):
                        for l in range(2):
                            obj3d.add(Vector3D(i*size,j*size,k*size,g*size,h*size,l*size))
    return obj3d
obj3d = Object3D()

objs = [cube(8), obj3d]

def put3DObjsIntoCanvas(canvas, objs):
    for e in objs:
        for o in e.getVectors():
            v = o.getVector()
            canvas.putLine(v[0][0]+v[0][2], v[0][1]+v[0][2], v[1][0]+v[1][2], v[1][1]+v[1][2], "\033[0;0;42m ")
def move(obj, x, y, z):
    for v in obj.getVectors():
        v.a[0]+=x
        v.a[1]+=y
        v.a[2]+=z
        v.b[0]+=x
        v.b[1]+=y
        v.b[2]+=z        
while True:
    time.sleep(0.4)
    canvas.clearCanvas()
    put3DObjsIntoCanvas(canvas, objs)
    canvas.drawCanvas()
    move(objs[0], 1, 1, 1)
