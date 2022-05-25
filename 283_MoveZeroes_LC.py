class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(nums)):
            if(nums[i]==0):
                count=count+1
            elif(count>0):
                nums[i-count]=nums[i]
                nums[i]=0
        return nums

    x=moveZeroes(1,[0,1,0,3,12])
    print(x)

    # https://leetcode.com/problems/move-zeroes/