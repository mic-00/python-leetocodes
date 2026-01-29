from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixCopy = [ matrix[i][:] for i in range(len(matrix)) ]
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                matrix[i][-j-1] = matrixCopy[j][i]