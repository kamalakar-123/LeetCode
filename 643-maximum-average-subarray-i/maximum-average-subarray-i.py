class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left=0
        right=k-1
        w_sum=sum(nums[left:right+1])
        max_sum=w_sum

        while right<len(nums)-1:
            w_sum-=nums[left]
            left+=1
            right+=1
            w_sum+=nums[right]
            max_sum=max(max_sum, w_sum)
        return max_sum/k