class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict ={}
        s2_dict ={}
        n = len(s1)
        m = len(s2)
        l = 0
        if m<n:
            return False

        for i in range(n):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        if s1_dict == s2_dict:
            return True

        for i in range(n,m):
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
            l+=1
            # print(s1_dict, s2_dict)

            if s1_dict == s2_dict:
                return True
        return False
            
        