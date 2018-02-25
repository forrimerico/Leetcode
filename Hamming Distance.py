#   0b101
# 0b11100

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # binX = bin(x)[::-1]
        # binY = bin(y)[::-1]
        # res = 0
        # lenX = len(binX)
        # lenY = len(binY)
        # dif = lenX-lenY
        # flag = 0
        # if dif < 0:
        #     dif = -dif
        #     flag = 1
        # replaceNum = 'b'
        # for i in range(dif):
        #     replaceNum += '0'
        #
        # if flag == 0:
        #     binY = binY.replace('b', replaceNum[::-1])
        # else:
        #     binX = binX.replace('b', replaceNum[::-1])
        # i = 0
        # while True:
        #     if binX[i] != binY[i]:
        #         res += 1
        #
        #     if binX[i] == 'b':
        #         return res
        #     i += 1
        return bin(x^y).count('1')

a = Solution()
b = a.hammingDistance(1,4)
print(b)

