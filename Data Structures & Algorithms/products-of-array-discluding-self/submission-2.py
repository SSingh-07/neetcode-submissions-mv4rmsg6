class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        res2 = [1]

        for i in nums[:-1]:
            res.append(res[-1]*i)   

        for i in nums[-1:0:-1]:
            res2.append(res2[-1]*i)
            
        res2.reverse()
        return [res[i]*res2[i] for i,j in enumerate(nums)]


        