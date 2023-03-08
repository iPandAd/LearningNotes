class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            rst = 0
            for j in range(i+1):
                rst = rst + nums[j]
            result.append(rst)
        return result
    
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums
