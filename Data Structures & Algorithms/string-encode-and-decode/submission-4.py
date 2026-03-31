class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""] or strs == []:
            return strs

        new_s = "''".join(strs)
        return new_s
        

    def decode(self, s: str) -> List[str]:
        
        if s==[""] or s==[]:
            return s
        new_list = s.split("''")
        return new_list
