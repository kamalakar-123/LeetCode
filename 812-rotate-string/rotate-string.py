class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        news=s
        for i in range(0,len(news)):
            if news==goal:
                return True
            news=news[-1]+news[:-1]
        return False