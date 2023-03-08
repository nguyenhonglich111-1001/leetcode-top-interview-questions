# NOTE 63.80%
class Solution:
    def isValid(self, s: str) -> bool:

        perfectLover = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        # Check len, first index invalid
        if s.__len__() % 2 or s[0] in perfectLover:
            return False

        coupleMatch = []

        # Push luver to stack and see if they match the next half
        for luver in s:
            if luver not in perfectLover:
                coupleMatch.append(luver)
            else:
                if coupleMatch.__len__() == 0:
                    return False
                    
                if perfectLover[luver] == coupleMatch[-1]:
                    coupleMatch.pop()
                else:
                    return False


        return coupleMatch.__len__() == 0