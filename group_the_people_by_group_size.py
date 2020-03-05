class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = {}
        final_list = []
        for r in range(len(groupSizes)):
            if groupSizes[r] in hm:
                hm[groupSizes[r]].append(r)
            else:
                hm[groupSizes[r]] = []
                hm[groupSizes[r]].append(r)
        for key in hm:
            if len(hm[key]) > key:
                for i in range(0, len(hm[key]), key):
                    final_list.append(hm[key][i: i+key])
            else:
                final_list.append(hm[key])
        return final_list
