class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left=0
        count=0
        for right in range(len(s)):
            window_size=right-left+1
            if window_size==3:
                if len(set(s[left:right+1]))==3:
                    count+=1
                left+=1
        return count
