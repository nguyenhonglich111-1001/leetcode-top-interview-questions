#  NOTE Beats 83.36%
def letterCombinations(self, digits: str) -> list[str]:
    letters = {
        2 : 'abc',
        3 : 'def',
        4 : 'ghi',
        5 : 'jkl',
        6 : 'mno',
        7 : 'pqrs',
        8 : 'tuv',
        9 : 'wxyz',
    }

    res = ['']

    def backtrack(index : int):
        
        if index == len(digits):
            return 
        
        while(len(res[0]) < index + 1):
            for letter in letters[int(digits[index])]:
                res.append(res[0] + letter)

            res.pop(0)
        backtrack(index + 1) 

    backtrack(0)

    if res[0] == '':
        return []

    return res