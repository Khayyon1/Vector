from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector:
    
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
    
    def dot_product(self, other):
        return sum([x * y for (x, y) in zip(self.coordinates, other.coordinates)])
    
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
    
    def times_scalar(self, c):
        new_coordinates = [Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)

if __name__ == '__main__':
    v5 = Vector((3.183, -7.627))
    v6 = Vector((-2.668, 5.319))
    
    print(v5.angle(v6, True))
    
    v7 = Vector((7.35, 0.221, 5.188))
    v8 = Vector((2.751, 8.259, 3.985)) 
    print(v7.angle(v8))