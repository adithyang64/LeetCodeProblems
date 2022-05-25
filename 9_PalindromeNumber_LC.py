class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number=x
        rev=0
        while(x>0):
            remainder=x%10
            rev=(rev*10)+remainder
            x=x//10
        print(rev)
        if(number==rev):
            a = True
        else:
            a = False
        print(a)
        return(a)

    x = isPalindrome(1,121)

    # https://leetcode.com/problems/palindrome-number/