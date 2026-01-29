# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from utils.list_node import ListNode

class Solution(object):
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        return self._createListNode(self._getNumber(l1) + self._getNumber(l2))
    
    def _getNumber(self, l: ListNode) -> int:
        def getNumberRecursive(l, i):
            n = l.val * 10 ** i
            if not l.next:
                return n
            return n + getNumberRecursive(l.next, i + 1)
        return getNumberRecursive(l, 0)
    
    def _createListNode(self, n: int) -> ListNode:
        def createListNodeRecursive(n, i, next = None):
            v = n // 10 ** i
            l = ListNode(v, next)
            if i == 0:
                return l
            return createListNodeRecursive(n - v * 10 ** i, i - 1, l)
        if n == 0:
            return ListNode(0)
        return createListNodeRecursive(n, int(math.log10(n)))