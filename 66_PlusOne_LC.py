from re import A


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x=0
        for i in digits:
            x=x*10
            x=x+i
        x=x+1
        a=list(str(x))
        print(a)
        return a
    x = plusOne(1,[1,2,3])        

    # https://leetcode.com/problems/plus-one/