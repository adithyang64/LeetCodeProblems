class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        list1=[]
        for j in range(0,n+1):
            count = 0
            while (j):
                count += j & 1
                j >>= 1
            list1.append(count)
        return list1

    x=countBits(1,9)
    print(x)

    # https://leetcode.com/problems/counting-bits/