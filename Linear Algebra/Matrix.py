class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def transform(self, vector):
        result = []
        for i in len(matrix):
            result.append(sum(self.matrix[i] * vector.vector))
        return Vector(result)
