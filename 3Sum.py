class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == [] or len(nums)<3:
            return []
        i = 0
        j = 1
        lens = len(nums)
        m = j
        results = []
        sDel = []
        while True:

            if j == lens - 1 and i != lens - 2:
                i += 1
                j = i + 1
                m = j

            if m != lens -1 or m == j:
                m += 1
            else: # m == lens - 1
                j += 1
                m = j + 1
                if j == lens - 1:
                    m -= 1
                    continue

            if j == lens - 1 and i == lens - 2:
                for Ri in range(len(results)):
                    for Rj in range(len(results)):
                        if Rj <= Ri:
                            continue
                        if sorted(results[Ri]) == sorted(results[Rj]):
                            if Rj not in sDel:
                                sDel.append(Rj)
                sDel = sorted(sDel)
                sDel.reverse()
                for Rd in sDel:
                    del results[Rd]

                return results

            if nums[m] == -(nums[i] + nums[j]):
                results.append([nums[m], nums[j], nums[i]])




a = Solution()
# results =[[6, -2, -4], [6, -2, -4], [6, -2, -4], [6, -2, -4], [6, -2, -4], [6, -2, -4], [4, 0, -4], [4, 0, -4], [3, 1, -4], [3, 1, -4], [2, 2, -4], [2, 2, -4], [2, 2, -4], [4, -2, -2], [4, -2, -2], [4, -2, -2], [4, -2, -2], [2, 0, -2], [2, 0, -2], [2, 0, -2], [4, -2, -2], [4, -2, -2], [2, 0, -2], [2, 0, -2], [2, 0, -2], [2, 0, -2], [2, 0, -2], [2, 0, -2]]
# sDel = []
# for Ri in range(len(results)):
#     for Rj in range(len(results)):
#         if Rj <= Ri:
#             continue
#         if sorted(results[Ri]) == sorted(results[Rj]):
#             if Rj not in sDel:
#                 sDel.append(Rj)

#sDel = sorted(sDel)
#sDel.reverse()
#print(sDel)
# for Rd in sDel:
#     del results[Rd]


print(a.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
