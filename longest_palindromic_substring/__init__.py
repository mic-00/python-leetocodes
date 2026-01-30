class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        def longestPalindromeRecursive(s, i, j):
            if self.__isPalindrome(s[i:j]):
                return s[i:j]
            s1, s2 = longestPalindromeRecursive(s, i, j - 1), longestPalindromeRecursive(s, i + 1, j)
            return max(s1, s2, key=len)
        return longestPalindromeRecursive(s, 0, len(s))
    
    def __isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        return s[0] == s[-1] and self.__isPalindrome(s[1:-1])