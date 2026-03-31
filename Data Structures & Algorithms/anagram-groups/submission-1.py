class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            res[''.join(sorted(i))].append(i)

        result = []
        for i in res:
            result.append(res[i])

        return result
        