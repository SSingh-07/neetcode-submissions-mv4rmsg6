class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxright = prices[-1]
        curr = 0
        res= 0
        for i in prices[::-1]:
            if maxright< i:
                maxright = i
            else:
                curr = maxright - i
            res = max(curr, res)
        return res
            



        