import math

class Solution(object):
    def intToRoman(self, num: int) -> str:
        if num < 1:
            return ""
        i = int(math.log10(num))
        d = int(num // 10 ** i)
        if d < 4:
            s = self._getSymbol(i) * d
        elif d == 4:
            s = self._getSymbolCase4(i)
        elif d == 5:
            s = self._getSymbolCase5(i)
        elif d < 9:
            s = self._getSymbolCase5(i) + self._getSymbol(i) * (d - 5)
        else:
            s = self._getSymbolCase9(i)
        return s + self.intToRoman(num - d * 10 ** i)
    
    def _getSymbol(self, i: int) -> str:
        if i == 0:
            return "I"
        if i == 1:
            return "X"
        if i == 2:
            return "C"
        return "M"
    
    def _getSymbolCase4(self, i: int) -> str:
        if i == 0:
            return "IV"
        if i == 1:
            return "XL"
        return "CD"
    
    def _getSymbolCase5(self, i: int) -> str:
        if i == 0:
            return "V"
        if i == 1:
            return "L"
        return "D"
    
    def _getSymbolCase9(self, i: int) -> str:
        if i == 0:
            return "IX"
        if i == 1:
            return "XC"
        return "CM"
