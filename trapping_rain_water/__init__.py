from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        t = [ 0 ] * len(height)
        for i in range(1, len(height)):
            prevHeight = height[i - 1] + t[i - 1]
            maxHeight = max(height[i:])
            if prevHeight > height[i] and maxHeight > height[i]:
                t[i] = min(prevHeight, maxHeight) - height[i]
        return sum(t)