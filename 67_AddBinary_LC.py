class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #Calculating binary value using function
        sum = bin(int(a, 2) + int(b, 2))
        print(sum)
        #o/p:0b100
        a=sum[2:] #Getting elements from 2nd element
        print(a)
        return(a)
    x=addBinary(1,"11","1")

    # https://leetcode.com/problems/add-binary/
