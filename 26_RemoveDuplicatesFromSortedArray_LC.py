class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        n=len(nums)
        for i in range(0,n-1):
            if(nums[i] != nums[i+1]):
                nums[j]=nums[i]
                j+=1
        nums[j]=nums[n-1]
        j+=1
        return j
    
    x = removeDuplicates(1,[1,1,2])
    print(x)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/