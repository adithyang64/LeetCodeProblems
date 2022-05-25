class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        i=0
        while i < (len(nums)-1):
            j=i+1
            while j < (len(nums)):
                if((nums[i]+nums[j])==target):
                    a.append(i)
                    a.append(j)
                    sum=nums[i]+nums[j]
                    print(sum)
                    print(a)
                j=j+1
            i=i+1
        return a

    x =twoSum(1,[3,2,4],6)

    # https://leetcode.com/problems/two-sum/