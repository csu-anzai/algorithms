# n-log_n, cost of solution
# Import for twoSum argument data structures
from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        # Left pointer
        l = 0

        #Right pointer
        r = len(nums) - 1

        # Looping right and left pointer to find first match 
        while l < r:
            current = nums[l] + nums[r]
            if current == target:
                return [nums[l], nums[r]]
            elif current < target:
                l += 1
            elif  current > target:
                r -= 1
        return[]







