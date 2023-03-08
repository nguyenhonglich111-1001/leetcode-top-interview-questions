# NOTE 9.32%
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        
        itlen = len(strs[0])
        strslen = len(strs)
        

        # Using 1 element as the pivot, compare through the rest array
        for i in range(1,itlen+1):
            
            samePrefix = True

            # Cut i character from rest and compare => low performance
            for j in range(1, strslen):
                if strs[0][:i] != strs[j][:i]:
                    samePrefix = False
                    break
                    
            if samePrefix:
                result = strs[0][:i]
            else:
                break
                
        
        return result
    

# NOTE 62.35%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        minStr = min(strs, key=len)
        minLen = len(minStr)
        strslen = len(strs)
        print(minLen)
        rightMost = -1
        # Using 1 element as the pivot, compare through the rest array
        for i in range(0,minLen):
            
            sameChar = True

            # Compare single by single character, 
            for j in range(1, strslen):
                if strs[0][i] != strs[j][i]:
                    sameChar = False
                    break
            # if i character of each string didn't match, break
            if not sameChar:
                break

            rightMost = i
                
        return strs[0][0:rightMost+1]
        