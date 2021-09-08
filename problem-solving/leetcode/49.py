'''
#ver 01 
class Solution(object):
    def groupAnagrams(self, strs):
        rtn = []
        tmp = [''.join(sorted(c)) for c in strs]
        for c in set(tmp):
            e = []
            for i in range(len(tmp)):
                if tmp[i] == c:
                    e.append(strs[i])
            rtn.append(e)
        return rtn
'''
from collections import defaultdict


# ver 02
class Solution(object):
    def groupAnagrams(self, strs):

        # value가 list인 형태의 dict를 반환
        a = defaultdict(list)

        for word in strs:
            a[''.join(sorted(word))].append(word)

        return list(a.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
