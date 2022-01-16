from math import factorial, sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector:
    # Parallel vectors are one vector time scalar equals another vector
    # Othogonal vectors are v1 times v2 = zero vector implies one of the vectors
    # is the zero vector or they are at right angle to each other

    # Zero vector is parallel and orthogonal to all vectors and only vector orthogonal to itself

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot divide by Zero'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
            
        except ValueError:
            raise ValueError('The coordinates must be homepage')
        
        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    
    def isOrthogonal(self, other, tolerance=1e-10):
        return True if abs(self.dot_product(other)) < tolerance else False

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def isParallel(self, other):
        return (self.is_zero() or
                other.is_zero() or
                self.angle(other) == 0 or
                self.angle(other) == pi)
    def dot_product(self, other):
        return sum([x * y for (x, y) in zip(self.coordinates, other.coordinates)])
    
    def roundCoordinates(self, places=3):
        self.coordinates = tuple(map(lambda x: round(x, places), self.coordinates))

    def angle(self, other, in_radians=False):
        if in_radians == True:
            return self.angle_in_radians(other)
        else:
            return self.angle_in_degrees(other)

    def angle_in_radians(self, other):
        norm_v = self.normalization()
        norm_w = other.normalization()
        return acos(norm_v.dot_product(norm_w))
    
    def angle_in_degrees(self, other):
        degrees_per_radian = 180. / pi
        radians = self.angle_in_radians(other)
        return degrees_per_radian * radians
    
    def magnitude(self):
            squared = [Decimal(x)**2 for x in self.coordinates]
            return sqrt(sum(squared))
    
    def normalization(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/ Decimal(magnitude))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, v):
        '''
            Checks if two vectors are equal to each other
        '''
        return self.coordinates == v.coordinates
    
    def __add__(self, other):
        self.coordinates = tuple(map(sum, zip(self.coordinates, other.coordinates)))
        return self
    
    def __sub__(self, other):
        self.coordinates = tuple(map(lambda x, y: x - y, self.coordinates, other.coordinates))
        return self


    def __mul__(self, scalar):
        self.coordinates = tuple(map(lambda x:scalar * x, self.coordinates))
        return self
    
    def __rmul__(self, scalar):
        self.coordinates = tuple(map(lambda x: x * scalar, self.coordinates))
        return self

    def __truediv__(self, other):
        c1 = self.coordinates
        c2 = other.coordinates
        return tuple(map(lambda x, y: x / y, c1, c2))[0]
    
    def times_scalar(self, c):
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

if __name__ == '__main__':
    v = Vector((2.118, 4.827))
    w = Vector((0, 0))

    print(v.isOrthogonal(w))
    print(v.isParallel(w))
