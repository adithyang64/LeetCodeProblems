class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

    x = removeElement(1,[3,2,2,2,3],3)
    print(x)

    #https://leetcode.com/problems/remove-element/