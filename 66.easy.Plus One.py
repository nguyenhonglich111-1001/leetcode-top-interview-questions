#NOTE Beats 58.96%
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in range(digits.__len__()-1,-1,-1):

            digits[i] += 1

            if digits[i] == 10:
                digits[i] = 0
            else:
                break

        if digits[0] == 0:
            return [1] + digits

        return digits