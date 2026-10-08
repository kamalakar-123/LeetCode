class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        newar=[]
        nums2_copy = nums2.copy()
        for i in nums1:
            if i in nums2_copy:
                newar.append(i)
                nums2_copy.remove(i)
        return newar