class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        maxtillday = 0
        for i in prices[::-1]:
            res = max(res, maxtillday - i)
            maxtillday = max(maxtillday, i)
        
        return res


        