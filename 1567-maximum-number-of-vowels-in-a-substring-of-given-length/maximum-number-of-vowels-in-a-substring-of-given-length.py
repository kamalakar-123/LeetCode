class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        right=k-1

        vowels='aeiou'
        count=0

        i=left
        while i<=right:
            if s[i]in vowels:
                count+=1
            i+=1
        max_count=count
        while right<len(s)-1:
            if s[left] in vowels:
                count-=1
            left+=1
            right+=1
            if s[right] in vowels:
                count+=1
            max_count=max(max_count, count)
        return max_count