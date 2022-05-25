class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        #print(count)
        for key,value in count.items():
            #print(value)
            if(value>=2):
                return True
        return False

    x=containsDuplicate(1,[1,2,3,1])
    print(x)

    # https://leetcode.com/problems/contains-duplicate/