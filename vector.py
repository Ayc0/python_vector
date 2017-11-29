from random import random

class Vector:
    def __init__(self, coord):
        x, y, z = coord
        self.x = x
        self.y = y
        self.z = z

    def coord(self):
        return (self.x, self.y, self.z)
    
    def __add__(first, second):
        if type(second) == Vector:
            a, b, c = first.coord()
            d, e, f = second.coord()
            return Vector((a + d, b + e, c + f))
        return first + second*ones()
    
    def __rmul__(vector, item):
        d, e, f = vector.coord()
        return Vector((item*d, item*e, item*f))

    def __radd__(vector, item):
        return vector + item
    
    def __mul__(first, second):
        if type(second) == Vector:
            d, e, f = first.coord()
            a, b, c = second.coord()
            return a*d + b*e + c*f
        else:
            return second*first

    def norm(self):
        return (self*self)**0.5

    def __truediv__(vector, scalar):
        if scalar == 0:
            return float('inf')*vector
        else:
            return (1/scalar)*vector
    
    def __sub__(vector1, vector2):
        return vector1 + (-1 * vector2)

    def __repr__(self):
        return 'Vector' + str(self.coord())
    
    def __str__(self):
        return '/ ' + str(self.x) + '\n| ' + str(self.y) + '\n\\ ' + str(self.z) + '\n'
    
    def __xor__(first, second):
        a, b, c = first.coord()
        d, e, f = second.coord()
        return Vector((b*f - e*c, c*d - f*a, a*e - b*d))

    def __neg__(self):
        return -1*self

    def __pos__(self):
        return self

    def __eq__(first, second):
        if type(second) != Vector:
            return False
        a, b, c = first.coord()
        d, e, f = second.coord()
        return a == d and b == e and c == f

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, key):
        if key == 0 or key == 'x':
            return self.x
        elif key == 1 or key == 'y':
            return self.y
        elif key == 2 or key == 'z':
            return self.z
        else:
            raise IndexError('index out of bounds')

    def __setitem__(self, key, value):
        if key == 0 or key == 'x':
            self.x = value
        elif key == 1 or key == 'y':
            self.y = value
        elif key == 2 or key == 'z':
            self.z = value
        else:
            raise IndexError('index out of bounds')

    def __pow__(vector1, vector2):
        final = []
        for x,y in zip(vector1, vector2):
            final.append(x*y)
        return Vector(final)
        
    def normalized(self):
        return self/self.norm()
        
def base():
    return Vector((1,0,0)),Vector((0,1,0)),Vector((0,0,1))

def rand():
    return Vector([random(), random(), random()])

def ones():
    return Vector((1,1,1))
    
