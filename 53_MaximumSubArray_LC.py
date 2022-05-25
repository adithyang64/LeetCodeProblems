class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = nums[0]
        minSum = 0
        sum=0
        for i in range(n):
            sum += nums[i]
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)
        return maxSum
        
    x = maxSubArray(1,[-2,1,-3,4,-1,2,1,-5,4])
    print(x)

    # https://leetcode.com/problems/maximum-subarray/
        