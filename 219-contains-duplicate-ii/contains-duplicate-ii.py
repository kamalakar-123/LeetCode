class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l=0
        r=0
        window=set()
        while r<len(nums):
            if nums[r] in window:
                return True
            window.add(nums[r])

            if r-l+1>k:
                window.remove(nums[l])
                l+=1
            r+=1
        return False