import math
from filecmp import cmp


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        list = {}
        num = 0

        if x >= 2 ** 31 or x <= -2 ** 31:
            return 0
        if x < 0:
            flag = -1
        else:
            flag = 1
        x = x * flag

        for i in range(32):
            if x < 10:
                num += 1
                list[i] = x % 10
                break
            else:
                num += 1
                list[i] = x % 10
                x = int(x / 10)

        for i in range(num):
            result = result + list[i] * pow(10, num - i - 1)

        if result >= 2**31:
            return 0

        return result * flag


t = Solution()
print(t.reverse(-12200301))