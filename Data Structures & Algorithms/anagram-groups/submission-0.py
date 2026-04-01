class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = [str(sorted(s)) for s in strs]
        output_dict = {key: [] for key in keys}
        for s in strs:
            output_dict[str(sorted(s))].append(s)
        result = [val for val in output_dict.values()]
        return result

        
            

        