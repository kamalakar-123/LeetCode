class Solution:
    def arraySign(self, nums: list[int]) -> int:
        res=1
        n=len(nums)
        for i in range (n):
            res=res*nums[i]
        if res >0:
            return 1
        elif res<0:
            return -1
        else:
            return 0
    
