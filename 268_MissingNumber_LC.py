class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum =0
        sum_n = (n*(n+1))/2
        print(sum_n)
        for i in nums:
            sum = sum+i
        print(sum)
        return (sum_n-sum)
    
    x=missingNumber(1,[3,0,1])
    print(x)

    # https://leetcode.com/problems/missing-number/