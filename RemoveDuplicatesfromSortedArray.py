class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lens = len(nums) - 1
        for i in range(lens, -1,-1):
            if i == 0:
                break
            if nums[i] == nums[i-1]:
                del nums[i]
        return nums
a = Solution()
print(a.removeDuplicates([1,1,1]))
