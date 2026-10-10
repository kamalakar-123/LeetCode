class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        left=0
        right=k-1
        count=0
        while right< len(s):
            value=int(s[left:right+1])
            if value!=0 and num % value==0:
                count+=1
            left+=1
            right+=1
        return count