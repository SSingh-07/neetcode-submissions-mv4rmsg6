class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        if not s:
            return 0
        length = 1
        curr = 0
        l = r = 0

        while r < len(s):
            while s[r] in check:
                curr -=1
                check.remove(s[l])
                l+=1
            else:
                curr+=1
                check.add(s[r])
                r+=1
            length = max(curr, length)
        return length
        