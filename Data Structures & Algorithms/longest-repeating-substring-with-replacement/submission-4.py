class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        check = defaultdict(int)
        length = len(s)
        maxfreq = 0
        maxlen = 0

        while r<length:
            check[s[r]]+=1
            maxfreq = max(maxfreq, check[s[r]])

            while (r-l+1) - maxfreq > k:
                check[s[l]]-=1
                l+=1
            
            maxlen = max(maxlen, r-l+1)
            r+=1

        return maxlen

            



        