import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        i = 1
        result = 0
        limit = int(math.sqrt(num))

        for i in range(1,limit + 1):
            if num % i == 0:
                print(i, end=' ')
                div = num // i
                print(div)
                if i == div or div == num:
                    result+=i
                else:
                    result+=i
                    result+=div
        return result == num

