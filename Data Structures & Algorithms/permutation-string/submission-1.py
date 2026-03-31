from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        slen = len(s1)
        s2len = len(s2)

        if not s1:
            return True
        if not s2 or s2len < slen:
            return False

        check = dict(Counter(s2[0:slen]))
        check2 = dict(Counter(s1))
        print(check, check2)
        if check==check2:
            return True

        l= 0
        for r in range(slen,s2len):
            check[s2[r]] = 1 + check.get(s2[r],0)
            check[s2[l]] -=1
            if check[s2[l]]==0:
                del check[s2[l]]
            l+=1


            if check == check2:
                return True

        return False




        




        
        