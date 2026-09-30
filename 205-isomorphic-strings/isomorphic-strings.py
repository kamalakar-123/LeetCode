class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dist = {}
        seen_t = set()

        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]

            if ch_s in dist:
                if dist[ch_s] != ch_t:
                    return False
            else:
                if ch_t in seen_t:
                    return False
                dist[ch_s] = ch_t
                seen_t.add(ch_t)

        return True