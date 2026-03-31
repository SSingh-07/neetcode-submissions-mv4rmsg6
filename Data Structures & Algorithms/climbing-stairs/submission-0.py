class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        

        def dfs(k):
            if k==0:
                res[0]+=1
                return 

            k -=2
            if k >=0:dfs(k)
            k+=2
            k-=1
            if k>=0:dfs(k)

        dfs(n)
        return res[0]
            


            

                    