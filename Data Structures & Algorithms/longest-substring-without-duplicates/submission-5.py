class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        check = set()
        length = len(s)
        curr = 0
        res = 0

        while r< length:
            if s[r] not in check:
                check.add(s[r])
                curr+=1
                r+=1
            else:
                while s[r] in check:
                    check.remove(s[l])
                    curr-=1
                    l+=1
            res = max(res, curr)

        return res
        
        