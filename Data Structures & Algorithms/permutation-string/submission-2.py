from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if not s1: return True
        if not s2: return False

        length1 = len(s1)
        length2 = len(s2)

        if length2 < length1: return False

        target = dict(Counter(s1))
        check = defaultdict(int)

        for i in range(length1):
            check[s2[i]]+=1
        print(check)

        if check == target:
            return True
        l=0
        r = length1
        while r< length2:
            check[s2[r]]+=1
            check[s2[l]]-=1
            if check[s2[l]]==0:
                del check[s2[l]]

            l+=1
            r+=1
            if target == check:
                return True
        return False



        