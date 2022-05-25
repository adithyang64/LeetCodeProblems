class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==0):
            return False
        else:
            while(n!=1):
                if(n%3!=0):
                    return False
                n=n/3
            return True

    x = isPowerOfThree(1,27)
    print(x)

    # https://leetcode.com/problems/power-of-three/