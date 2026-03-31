from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter([i for i in s])
        tt = Counter([j for j in t])

        return ss==tt


        