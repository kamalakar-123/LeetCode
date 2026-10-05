class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        curr=0
        stack=[]
        for bras in s:
            if bras=="(":
                stack.append("(")
                curr+=1
                maxi=max(maxi,curr)
            elif bras==")":
                curr-=1
                stack.pop()
        return maxi