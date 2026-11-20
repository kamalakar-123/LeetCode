class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if nums==sorted(nums):
            return True
        if nums==sorted(nums,reverse=True):
            return True
        return False
        