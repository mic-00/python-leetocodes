import unittest
from add_two_numbers import Solution as AddTwoNumbersSolution
from integer_to_roman import Solution as IntegerToRomanSolution
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

if __name__ == "__main__":
    unittest.main()