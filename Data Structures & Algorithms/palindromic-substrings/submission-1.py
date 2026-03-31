class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [0]
        length = len(s)

        def count_palind(l,r,length):
            while 0<=l and r<length and s[l]==s[r]:
                res[0]+=1
                l-=1
                r+=1

        for i in range(length):
            l = r = i
            count_palind(l,r,length)

            l = i
            r = i+1
            count_palind(l,r,length)
            
        
        

        return res[0]
