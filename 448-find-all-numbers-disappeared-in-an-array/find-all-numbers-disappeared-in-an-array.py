class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        a = []
        b = set(nums)

        for i in range(1, n + 1):
            if i not in b:
                a.append(i)

        return a