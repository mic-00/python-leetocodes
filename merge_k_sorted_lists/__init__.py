# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from typing import List
from utils.list_node import ListNode

class Solution(object):
    def mergeKLists(self, lists: List[ListNode | None]) -> ListNode | None:
        while None in lists:
            i = lists.index(None)
            lists.pop(i)
        if len(lists) == 0:
            return None
        min_idx, min_val = 0, math.inf
        for k, v in enumerate(lists):
            if v.val < min_val:
                min_idx = k
                min_val = v.val
        lists[min_idx] = lists[min_idx].next
        return ListNode(min_val, self.mergeKLists(lists))
