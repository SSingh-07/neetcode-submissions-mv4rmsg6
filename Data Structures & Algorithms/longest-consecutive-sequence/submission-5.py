class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check = set(nums)
        res = 1
        

        for i in check:
            curr = 1
            j = i
            if j+1 not in check:
                while j-1 in check:
                    curr+=1
                    j-=1
            res = max(curr,res)

        return res
                

        