class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        lens = len(nums)
        for i in range(lens - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            m = lens - 1
            while j < m:
                s = nums[i] + nums[j] + nums[m]
                if s < 0:
                    j+=1
                elif s > 0 :
                    m -= 1
                else:
                    res.append([nums[i], nums[j], nums[m]])
                    while j < m and nums[j] == nums[j+1]:
                        j+=1
                    while j < m and nums[m] == nums[m-1]:
                        m-=1
                    j+=1
                    m-=1


        return res
        # if nums == [] or len(nums)<3:
        #     return []
        # nums = sorted(nums)
        # i = 0
        # j = 1
        # lens = len(nums)
        # m = j
        # results = []
        # while True:
        #
        #     if j == lens - 1 and i != lens - 2:
        #         i += 1
        #         j = i + 1
        #         m = j
        #
        #     if m != lens -1 or m == j:
        #         m += 1
        #     else: # m == lens - 1
        #         j += 1
        #         m = j + 1
        #         if j == lens - 1:
        #             m -= 1
        #             continue
        #
        #     if j == lens - 1 and i == lens - 2:
        #         return results
        #
        #     if nums[m] == -(nums[i] + nums[j]):
        #         if [nums[i], nums[j], nums[m]] in results:
        #             continue
        #         results.append([nums[i], nums[j], nums[m]])




a = Solution()

print(a.threeSum([0,0,0,0]))
