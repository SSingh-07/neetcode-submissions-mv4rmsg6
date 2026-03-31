class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        length = len(s)

        def dfs(i):
            if i >= length:
                res.append(curr.copy())
                return 

            for j in range(i, length):
                if self.palind(s, i, j):
                    curr.append(s[i: j+1])
                    dfs(j+1)
                    curr.pop()

        dfs(0)
        return res

    def palind(self, s, i, j):
        l = i
        r = j

        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l+1, r-1

        return True


            


        