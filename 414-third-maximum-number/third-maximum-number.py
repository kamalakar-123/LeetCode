class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        f, s, t = float('-inf'), float('-inf'),float('-inf')
        for num in nums:
            if num > f:
                f, s, t = num, f,s
            elif f>num>s:
                s,t=num,s
            elif s>num>t:
                t=num

        if t!=float('-inf'):
            return t
        else:
            return f