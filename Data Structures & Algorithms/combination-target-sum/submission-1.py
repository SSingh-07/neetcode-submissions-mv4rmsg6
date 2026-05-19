class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        length = len(nums)

        def dfs(i, summ):
            if summ == target:
                res.append(subset.copy())
                return

            if i>=length or summ> target:
                return

            subset.append(nums[i])
            summ+=nums[i]
            dfs(i,summ)
            subset.pop()
            summ-=nums[i]
            dfs(i+1, summ)
        

        dfs(0, 0)
        return res
        

            

        