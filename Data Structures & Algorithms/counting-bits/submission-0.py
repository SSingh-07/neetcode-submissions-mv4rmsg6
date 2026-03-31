class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            t = bin(i)
            res.append(t.count("1"))

        return res
        