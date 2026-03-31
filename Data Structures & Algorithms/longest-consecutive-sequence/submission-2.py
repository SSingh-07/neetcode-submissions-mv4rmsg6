class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        if check == set():
            return 0
        currmax = 1
        maxx = 1

        for i in check:
            k = i
            if k-1 in check and k+1 not in check:
                while k-1 in check:
                    currmax+=1
                    k-=1
                maxx= max(maxx, currmax)
                currmax =1
        return maxx
            

        