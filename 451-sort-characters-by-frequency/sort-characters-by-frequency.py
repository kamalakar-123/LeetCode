class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        hash_map={}
        for ch in s:
            hash_map[ch]=hash_map.get(ch,0)+1
        sorted_hash=sorted(hash_map.items(), key=lambda x:(-x[1],x[0]))
        for ch, freq in sorted_hash:
            res=res+(ch*freq)
        return res