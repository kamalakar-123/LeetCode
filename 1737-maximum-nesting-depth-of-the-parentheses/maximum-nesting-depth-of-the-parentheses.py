class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        curr = 0

        for char in s:
            if char == "(":
                curr += 1
                maxi = max(maxi, curr)
            elif char == ")":
                curr -= 1

        return maxi