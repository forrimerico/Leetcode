class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        i = 0
        while True:
            if strs == []:
                return result

            if i == len(strs[0]):
                return result

            temp = strs[0][i]

            for str in strs:
                if i == len(str):
                    return result

                if str[i] == temp:
                    continue
                else:
                    return result
            result = result + temp
            i = i+1

a = Solution()
print(a.longestCommonPrefix([]))