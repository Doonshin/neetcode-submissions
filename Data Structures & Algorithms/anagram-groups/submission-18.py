class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_map = {}
        for string in strs:
            sortedS = ''.join(sorted(string))
            if not sortedS in sort_map:
                sort_map[sortedS] = []
            sort_map[sortedS].append(string)

        return list(sort_map.values())    
 
        