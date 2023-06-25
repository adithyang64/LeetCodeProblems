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

    ## Another Approach

    # s=[3,0,1]
    # sorted_s = sorted(s)
    # print(sorted_s)
    
    # for i in range(len(sorted_s)-1):
    #     if not (sorted_s[i+1]==sorted_s[i]+1):
    #         a=sorted_s[i]
    #         b=sorted_s[i+1]
    #         for j in range(a+1,b,1):
    #             print(j)

    # https://leetcode.com/problems/missing-number/
