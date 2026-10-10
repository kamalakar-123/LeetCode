class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left=0
        right=k-1
        w_sum=sum(arr[:k])
        count=0
        if w_sum/k >=threshold:
            count+=1
        while right<len(arr)-1:
            w_sum-=arr[left]
            left+=1
            right+=1
            w_sum+=arr[right]

            if w_sum/k >=threshold:
                count+=1
        return count