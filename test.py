import math
import unittest
from add_two_numbers import Solution as AddTwoNumbersSolution
from integer_to_roman import Solution as IntegerToRomanSolution
from jump_game_2 import Solution as JumpGame2Solution
from longest_palindromic_substring import Solution as LongestPalindromicSubstringSolution
from utils.list_node import ListNode

class TestAddTwoNumbersSolution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAddTwoNumbersSolution, self).__init__(*args, **kwargs)
        self.s = AddTwoNumbersSolution()
    
    def test_1(self):
        l1 = ListNode.fromValues(2, 4, 3)
        l2 = ListNode.fromValues(5, 6, 4)
        self.assertEqual(self.s.addTwoNumbers(l1, l2).getStringRepresentation(), "7 -> 0 -> 8")
    
    def test_2(self):
        l1 = ListNode.fromValues(0)
        l2 = ListNode.fromValues(0)
        self.assertEqual(self.s.addTwoNumbers(l1, l2).getStringRepresentation(), "0")
    
    def test_3(self):
        l1 = ListNode.fromValues(9, 9, 9, 9, 9, 9, 9)
        l2 = ListNode.fromValues(9, 9, 9, 9)
        self.assertEqual(self.s.addTwoNumbers(l1, l2).getStringRepresentation(), "8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1")

class TestIntegerToRomanSolution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIntegerToRomanSolution, self).__init__(*args, **kwargs)
        self.s = IntegerToRomanSolution()
    
    def test_1(self):
        self.assertEqual(self.s.intToRoman(3749), "MMMDCCXLIX")
    
    def test_2(self):
        self.assertEqual(self.s.intToRoman(58), "LVIII")
    
    def test_3(self):
        self.assertEqual(self.s.intToRoman(1994), "MCMXCIV")

class TestJumpGame2Solution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestJumpGame2Solution, self).__init__(*args, **kwargs)
        self.s = JumpGame2Solution()
    
    def test_1(self):
        self.assertEqual(self.s.jump([ 2, 3, 1, 1, 4 ]), 2)
    
    def test_2(self):
        self.assertEqual(self.s.jump([ 2, 3, 1, 5, 1, 1, 1 ]), 3)
    
    def test_3(self):
        self.assertEqual(self.s.jump([ 0, 1 ]), math.inf)
    
    def test_4(self):
        self.assertEqual(self.s.jump([ 1 ]), 0)

class TestLongestPalindromicSubstringSolution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLongestPalindromicSubstringSolution, self).__init__(*args, **kwargs)
        self.s = LongestPalindromicSubstringSolution()
    
    def test_1(self):
        self.assertEqual(self.s.longestPalindrome("babad"), "bab")
    
    def test_2(self):
        self.assertEqual(self.s.longestPalindrome("cbbd"), "bb")

if __name__ == "__main__":
    unittest.main()