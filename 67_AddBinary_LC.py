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
        a=sum[2:]
        print(a)
        return(a)
    x=addBinary(1,"11","1")

    # https://leetcode.com/problems/add-binary/