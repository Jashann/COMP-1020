import numpy as np

class Matrix:

    def __init__(self, array):
        self.array = array
        self.rows = len(array)
        self.cols = len(array[0])

    def __str__(self):
        out = ""
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                out += str(self.array[i][j])+"   "
            out += "\n"
        
        return out

    def addition(self, other):

        if self.rows == other.rows and self.cols == other.cols:

            result = np.zeros((self.rows, self.cols), dtype=np.int64)

            for i in range(len(self.array)):
                for j in range(len(self.array[i])):
                    result[i][j] = self.array[i][j] + other.array[i][j]
        else:
            result = -1

        return result
        

# main
npArr = np.array([[1,2,3,4], [5,6,7,8]])
npArr2 = np.array([[1,2,3,4], [5,6,7,8]])

matrix1 = Matrix(npArr)
matrix2 = Matrix(npArr2)

matrix3 = matrix1.addition(matrix2)

print(matrix3)



