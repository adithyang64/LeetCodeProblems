class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while(low<=high):
            middle=(low+high)//2
            #print("233-" + str(middle))
            x=nums[middle]
            if(x==target):
                rtype=middle
                return rtype
            elif(x>target):
                a = middle
                high=middle-1
            elif(x<target):
                a = middle + 1
                low=middle+1
        return a

    x=searchInsert(1,[1,3,5,7,9],6)
    print(x)

    # https://leetcode.com/problems/search-insert-position/