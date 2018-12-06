class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_number = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }

        result = ['']
        temp = []

        for digit in digits:
            letters = digit_number.get(digit)
            for prefix in result:
                for letter in letters:
                    temp.append(prefix+letter)
            result = temp
            temp = []
            #result = [prefix+letter for prefix in result for letter in letters]
        return result
