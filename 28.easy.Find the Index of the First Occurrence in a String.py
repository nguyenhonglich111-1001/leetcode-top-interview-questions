# NOTE 5.14%
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Return first appear of needle in haystack

        # So this solution is just simply brute force, but even in bad way.
        haystack += '2'
        hlen = len(haystack)
        nlen = len(needle)
        for i in range(hlen - nlen):
            
            n = 0
            for j in range(i,i+nlen):
                if needle[n] == haystack[j]:
                    n += 1
                else:
                    n = 0

            if n == len(needle):
                return i

        return -1
    

# NOTE Beats 21.1% with just a single break
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        haystack += '2'
        # print(haystack)
        hlen = len(haystack)
        nlen = len(needle)
        for i in range(hlen - nlen):
            
            n = 0
            for j in range(i,i+nlen):
                if needle[n] == haystack[j]:
                    n += 1
                else:
                    break
                # print(haystack[i],n)
            # print('----------',n)

            if n == len(needle):
                return i

        return -1
    

#NOTE Beats 67.90%
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack += ' '
        starts = []

        h = len(haystack)
        n = len(needle)

        # Remember the needle[0] in haystack and use it to compare later
        for i in range(h - n):
            if haystack[i] == needle[0]:
                starts.append(i)

        # print(starts)
        for start in starts:
            # print(haystack[start:n])
            if haystack[start:start+n] == needle:
                return start

        return -1