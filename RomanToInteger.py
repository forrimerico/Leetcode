class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        baseRoman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        lens = len(s)
        for i,v in enumerate(s):
            flag = 1
            if i < lens-1:
                if baseRoman[s[i]] < baseRoman[s[i+1]]:
                    flag = -1

            result = result + flag * baseRoman[v]

        return result

a = Solution()
b = a.romanToInt('MCDXXXVII')
print(b)
