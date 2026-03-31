class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        total = len(s)
        l = 0
        maxfreq = 0
        res = 0

        for r in range(total):
            check[s[r]] = check.get(s[r], 0) + 1
            maxfreq = max(maxfreq, check[s[r]])

            if (r - l + 1 ) - maxfreq > k:
                check[s[l]] -= 1
                l+=1
            else:
                res = max(res, r - l + 1)
        return res
            


            

