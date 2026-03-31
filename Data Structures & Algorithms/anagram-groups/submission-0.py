class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for i in strs:
            if "".join(sorted(i)) in data:
                data["".join(sorted(i))].append(i)
            else:
                data["".join(sorted(i))] = [i]

        return data.values()
        