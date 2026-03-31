class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i, j in enumerate(nums):
            if i>0:
                res.append(res[i-1]*nums[i-1])
        l = i
        res2= [1]*(l+1)

        for k in range(l,-1,-1):
            if k<l:
                res2[k]=res2[k+1]*nums[k+1]
        return [res[i]*res2[i] for i in range(l+1)]
        