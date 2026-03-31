class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        max_len = 0

        if not nums:
            return 0

        data  = Counter(nums)

        for i in data:
            if i+1 not in data:
                j = i
                curr=0
                while j in data:
                    curr+=1
                    j-=1
                max_len = max(curr, max_len)

        return max_len

        
        