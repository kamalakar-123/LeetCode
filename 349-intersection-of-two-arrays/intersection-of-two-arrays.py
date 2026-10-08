class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        newar=[]
        for i in nums1:
            if i in nums2:
                if i not in newar:
                     newar.append(i)
        return newar
