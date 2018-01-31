class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,j in enumerate(nums):
            m = target - nums[i]
            if m in d:
                return [d[m],i]
            else:
                d[nums[i]] = i

t = Solution()
print(t.twoSum([5,4,3,1,2], 4))


