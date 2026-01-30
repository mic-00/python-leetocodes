from typing import List
import math

class Solution:
    def __init__(self):
        self.symbols = [ "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
        self.prime_numbers = [ 2, 3, 5, 7, 11, 13, 17, 19, 23 ]
        self.prod = 223092870 # 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ board[i][:] for i in range(9) ]
        columns = [ [ board[j][i] for j in range(9) ] for i in range(9) ]
        boxes = [ sum([ board[j+3*(i//3)][3*i%3:3*i%3+3] for j in range(3) ], []) for i in range(9) ]
        for group in [ *rows, *columns, *boxes ]:
            if not self.__isValidGroup(group):
                return False
        return True
    
    def __isValidGroup(self, group: List[str]):
        symbols = [ int(i) - 1 for i in group if i in self.symbols ]
        prime_numbers = [ self.prime_numbers[i] for i in symbols ]
        return len(prime_numbers) == 0 or self.prod % math.prod(prime_numbers) == 0