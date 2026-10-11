class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        large=float('-inf')
        scdlarge=float('-inf')
        for i in range(len(nums)):
            if nums[i]>=large:
                scdlarge=large
                large=nums[i]
                
            elif large>nums[i]>=scdlarge:
                scdlarge=nums[i]
        return (large-1)*(scdlarge-1)