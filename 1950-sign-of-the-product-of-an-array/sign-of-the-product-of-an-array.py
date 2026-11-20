class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0
        s=1
        for num in nums:
            if num<0:
                s=-s
        return s
