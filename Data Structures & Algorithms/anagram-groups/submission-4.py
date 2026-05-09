class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for i in strs: 
            check[''.join(sorted(i))].append(i)
        return list(check.values())

       
        
        
        