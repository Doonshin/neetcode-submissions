

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
        fre_map = defaultdict(list)
        for s in strs:
            fre = [0]*26
            for c in s:
                fre[ord(c) - ord('a')] += 1

            fre_map[tuple(fre)].append(s)
        return list(fre_map.values())