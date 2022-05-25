class Solution(object):
    def majorityElement(self, nums):
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
            ans= max(count, key=count.get)
            return ans
    x=majorityElement(1,[2,2,1,1,1,2,2])
    print(x)

    # https://leetcode.com/problems/majority-element/