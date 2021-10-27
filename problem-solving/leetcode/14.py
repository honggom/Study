class Solution:
    def longestCommonPrefix(self, strs):
        ''' 
        # 첫 풀이
        if strs[0] == "":
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        result = strs[0][0]
        
        for s in strs:
            if s == "" or s[0] != result:
                return ""
        
        for i in range(1, len(max(strs))):
            try:
                cur = strs[0][i]
                for st in strs:
                    if st[i] != cur:
                        return result
            except: 
                return result
            result += cur
            
        return result 
        '''
        
        # Better way
        result = []
        
        for x in zip(*strs):
            if len(set(x)) == 1: 
                result.append(x[0]) 
            else: 
                break 
        return "".join(result)
