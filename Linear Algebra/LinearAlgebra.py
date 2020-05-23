import numpy as np
import math

class DimensionMismatchError(Exception):
    pass

class Vector:
    def __init__(self, vector):
        self.vector = np.array(vector)
        # self.magnitude = self.magnitude()

    def __add__(self, vector):
        if len(self.vector) == len(vector):
            return Vector(self.vector + vector.vector)
        else:
            raise DimensionMismatchError('Vectors have different dimensions')

    def __rmul__(self, x):
        # x must be a scalar
        return Vector(self.vector * x)

    def __len__(self):
        return len(self.vector)

    def __str__(self):
        return str([int(i) if i%1==0 else float(i) for i in self.vector]).replace(',', '')

    # FIX METHOD
    @staticmethod
    def linearly_independent(vectors):
        # accept list of vectors
        n = len(vectors)
        for i in range(n):
            for j in range(i):
                if vectors[i].dot(vectors[j]): return False
        return True

    def dot(self, vector):
        return float(sum(self.vector * vector.vector))

    def scalar_projection(self, vector):
        return (self.dot(vector)) / vector.magnitude()

    def vector_projection(self, vector):
        return vector.normalize() * self.scalar_projection(vector)

    def magnitude(self):
        return math.sqrt(sum(self.vector ** 2))

    def magnitude_squared(self):
        return sum(self.vector ** 2)

    def normalize(self):
        # normalizes vector by magnitude to make it a unit vector
        return Vector(self.vector / self.magnitude())

class Matrix:
    def __init__(self, matrix, precision = 3):
        self.matrix = np.round(matrix, precision)
        self.m = self.matrix.shape[0]
        self.n = self.matrix.shape[1]
        self.precision = precision

    def __str__(self):
        anyFloats = np.any(self.matrix%1 != 0)
        maximum = np.max(self.matrix)
        result = ''

        if anyFloats:
            max_integer_width = str(maximum).index('.') if ('.' in str(maximum)) else len(str(maximum))
            max_decimal_width = self.precision
            padding = str(maximum).index('.')
            n = len(self.matrix)

            for i in range(n):
                row = self.matrix[i]
                if i > 0:
                    result += ' '

                integer_width = str(i).index('.') if ('.' in str(i)) else len(str(i))
                decimal_width = len(str(i)) - integer_width - 1

                result += str([((' ' * (max_integer_width - integer_width)) + str(i[:integer_width]) + '.' + str(i[integer_width:]) + ('0' * (max_decimal_width - decimal_width))) for i in row]).replace(',','').replace('\'','')

                if i < n - 1:
                    result += '\n'
            return result + ']'

        else:
            max_integer_width = len(str(maximum))
            result = '['
            n = len(self.matrix)
            for i in range(n):
                row = self.matrix[i]
                if i > 0:
                    result += ' '

                result += str([(' ' * (max_integer_width - len(str(i)))) + str(int(i)) for i in row]).replace(',','').replace('\'','')

                if i < n - 1:
                    result += '\n'
            return result + ']'


    def transform(self, vector):
        if self.n == len(vector.vector):
            result = []
            for i in range(self.m):
                result.append(sum(self.matrix[i] * vector.vector))
            return Vector(result)
        else:
            raise DimensionMismatchError('Matrix row dimension must equal vector dimension')

    def transpose(self):
        result = np.zeros((self.n, self.m))
        for i in range(self.m):
            result[:, i] = self.matrix[i, :]
        return Matrix(result)

    def inverse():
        pass


v1 = Vector([2, 3])
v2 = Vector([3, 2])
v3 = Vector([3, 8])
v4 = 3 * (v1 + v2)
# v3 = v3 * v1


vector = Vector([3, 4, 5])

matrix = Matrix([
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 1.2]
])

transformed = matrix.transform(vector)
transposed = matrix.transpose()

print(transformed)
print(transposed)
