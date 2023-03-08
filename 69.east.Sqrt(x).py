class Solution(object):
    def mySqrt(self, x):
        def binary_search(x) -> int:

            def condition(c) -> bool: 

                if c*c == x:
                    return False
                return c*c > x

            left, right = 1, x+1 # could be [0, n], [1, n] etc. Depends on problem
            while left < right:
                mid = left + (right - left) // 2
                print(left,right)
                if condition(mid):
                    right = mid
                else:
                    left = mid + 1

            return left-1


        return binary_search(x)