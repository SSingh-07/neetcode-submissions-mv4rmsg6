class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        substring = set()
        currlength, maxlength = 0, 0
        for i in s:
            if i in substring:
                while i in substring:
                    substring.remove(s[start])
                    currlength -=1
                    start +=1
                substring.add(i)
                currlength +=1
            
            else:
                substring.add(i)
                currlength +=1
                maxlength = max(maxlength, currlength)
        return maxlength





