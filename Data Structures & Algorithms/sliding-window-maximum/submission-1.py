from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        check = Counter(nums[0:k])
        res = [max(check)]
        l = 0
        for r in range(k,len(nums)):
            check[nums[r]] = 1 + check.get(nums[r],0)
            check[nums[l]] -=1
            if check[nums[l]] == 0:
                del check[nums[l]]
            l+=1
            res.append(max(check))

        return res

        