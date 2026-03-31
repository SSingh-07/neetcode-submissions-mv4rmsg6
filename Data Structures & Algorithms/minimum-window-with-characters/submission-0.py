from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        length = len(s)
        
        countT, window = {}, {}
        countT = dict(Counter(t))
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(length):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have+=1

            while have == need:

                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]]>window[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l:r+1] if resLen!=float('inf') else ""






        