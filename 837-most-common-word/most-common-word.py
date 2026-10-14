class Solution:
    def mostCommonWord(self, pa: str, ba: list[str]) -> str:
     
       mapp = {}
       maxi = float('-inf')
       temp = ""
       pa  = pa.lower()
       for i in range(len(ba)):
            ba[i] = ba[i].lower()
       pa = pa.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("'", " ")
       pa = pa.split()
       for i in pa :
            if i not in ba :
                mapp[i] = mapp.get(i,0)+1
       for i in mapp :
            if maxi <= mapp[i]:
               maxi = mapp[i]
               temp = i
       return temp
            
       