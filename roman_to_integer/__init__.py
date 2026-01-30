class Solution(object):
    def romanToInt(self, s: str) -> int:
        i, n = 0, 0
        while i < len(s):
            v1 = self.__getValue(s[i])
            if i + 1 < len(s):
                v2 = self.__getValue(s[i+1])
            else:
                v2 = v1
            if v1 < v2:
                n += v2 - v1
                i += 1
            else:
                n += v1
            i += 1
        return n
    
    def __getValue(self, c: str) -> int:
        if c == "I":
            return 1
        elif c == "V":
            return 5
        elif c == "X":
            return 10
        elif c == "L":
            return 50
        elif c == "C":
            return 100
        elif c == "D":
            return 500
        elif c == "M":
            return 1000
        raise Exception(f"Character {c} is not a valid symbol.")