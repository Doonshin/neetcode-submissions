

# defaultdictを使わないversion
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         sort_map = {}
#         for string in strs:
#             sortedS = ''.join(sorted(string))
#             if not sortedS in sort_map:
#                 sort_map[sortedS] = []
#             sort_map[sortedS].append(string)

#         return list(sort_map.values())    
 
        

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)

        return list(res.values())
