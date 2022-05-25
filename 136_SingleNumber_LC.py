class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        print(count)
        for key,value in count.items():
            print(key)
            if(value==1):
                print(key)
                return key
        
    x=singleNumber(1,[4,1,2,1,2])

    # https://leetcode.com/problems/single-number/