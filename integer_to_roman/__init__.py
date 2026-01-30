import math

class Solution(object):
    def intToRoman(self, num: int) -> str:
        if num < 1:
            return ""
        i = int(math.log10(num))
        d = int(num // 10 ** i)
        if d < 4:
            s = self.__getSymbol(i) * d
        elif d == 4:
            s = self.__getSymbolCase4(i)
        elif d == 5:
            s = self.__getSymbolCase5(i)
        elif d < 9:
            s = self.__getSymbolCase5(i) + self.__getSymbol(i) * (d - 5)
        else:
            s = self.__getSymbolCase9(i)
        return s + self.intToRoman(num - d * 10 ** i)
    
    def __getSymbol(self, i: int) -> str:
        if i == 0:
            return "I"
        if i == 1:
            return "X"
        if i == 2:
            return "C"
        return "M"
    
    def __getSymbolCase4(self, i: int) -> str:
        if i == 0:
            return "IV"
        if i == 1:
            return "XL"
        return "CD"
    
    def __getSymbolCase5(self, i: int) -> str:
        if i == 0:
            return "V"
        if i == 1:
            return "L"
        return "D"
    
    def __getSymbolCase9(self, i: int) -> str:
        if i == 0:
            return "IX"
        if i == 1:
            return "XC"
        return "CM"
