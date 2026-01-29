from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchMatrixRecursive(matrix: List[List[int]], target: int, i: int) -> bool:
            if i < 0 or i >= len(matrix):
                return False
            row = matrix[i]
            if target < row[0]:
                return searchMatrixRecursive(matrix, target, i - 1)
            if target > row[len(row)-1]:
                return searchMatrixRecursive(matrix, target, i + 1)
            return self.searchRow(row, target)
        return searchMatrixRecursive(matrix, target, len(matrix) // 2)
    
    def searchRow(self, row: List[int], target: int) -> bool:
        def searchRowRecursive(row: List[int], target: int, idx: int, prevIdx: int) -> bool:
            if idx < 0 or idx >= len(row):
                return False
            value = row[idx]
            if target < value:
                return idx <= prevIdx and searchRowRecursive(row, target, idx - 1, idx)
            if target > value:
                return idx >= prevIdx and searchRowRecursive(row, target, idx + 1, idx)
            return True
        return searchRowRecursive(row, target, len(row) // 2, len(row) // 2)