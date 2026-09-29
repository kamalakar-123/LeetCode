class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        max_reach = 0
        
        i = 0
        while i < n:
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            i = i + 1
        return True