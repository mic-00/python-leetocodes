import math
from typing import List

class Solution(object):
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        min = math.inf
        for i in range(1, nums[0] + 1):
            if i > len(nums):
                break
            j = self.jump(nums[i:])
            if j < min:
                min = j
        return 1 + min