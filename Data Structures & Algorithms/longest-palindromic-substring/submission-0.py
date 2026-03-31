class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [""]
        length = len(s)

        def count_palind(l, r):
            while 0<=l and r<length and s[l]==s[r]:
                if r+1 - l > len(res[0]):
                    res[0] = s[l:r+1]
                l-=1
                r+=1

        for i in range(length):
            l=r=i
            count_palind(l,r)
            l=i
            r=i+1
            count_palind(l,r)

        return res[0]


        