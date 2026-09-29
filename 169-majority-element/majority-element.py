class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        maxi=max(freq, key=freq.get)
        return maxi