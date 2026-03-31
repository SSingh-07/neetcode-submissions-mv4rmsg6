class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 1
        check = set(nums)

        for i in check:
            curr= 1
            l = i
            if i+1 not in check:
                while l-1 in check:
                    curr+=1
                    l-=1
                
            res= max(res, curr)

        return res

        