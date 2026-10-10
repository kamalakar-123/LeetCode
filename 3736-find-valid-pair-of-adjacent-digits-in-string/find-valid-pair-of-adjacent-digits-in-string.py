class Solution:
    def findValidPair(self, s: str) -> str:
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                if int(h[s[i]])==int(s[i]) and int(h[s[i+1]])==int(s[i+1]):
                    a=str(s[i])+str(s[i+1])
                    return a
        return ""