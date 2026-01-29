from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        stop, idxList, threeSumList = len(nums), [], []
        if stop >= 3:
            for i in range(stop):
                for j in range(i + 1, stop):
                    for k in range(j + 1, stop):
                        idxList.append([ i, j, k ])
            for idx in idxList:
                threeSum = [ nums[i] for i in idx ]
                threeSum.sort()
                if sum(threeSum) == 0 and threeSum not in threeSumList:
                    threeSumList.append(threeSum)
        return threeSumList