class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for i in J:
            res = res + S.count(i)
        return res
a = Solution()
print(a.numJewelsInStones('aA','aAAAbb'))

