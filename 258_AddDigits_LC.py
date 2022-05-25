class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num>9):
            x=num%10
            num/=10
            num=num+x
        return num

    x = addDigits(1,38)
    print(x)

    # https://leetcode.com/problems/add-digits/