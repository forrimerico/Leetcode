class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        for i in range(len(str(x))):
            if str(x)[i] == str(x)[-(i+1)]:
                continue
            else:
                return False

        return True
a = Solution()
print(a.isPalindrome(123321))