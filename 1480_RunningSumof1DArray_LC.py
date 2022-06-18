class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return(nums)
            
    ans = runningSum(1,[1,2,3,4])
    print(ans)

# https://leetcode.com/problems/running-sum-of-1d-array/