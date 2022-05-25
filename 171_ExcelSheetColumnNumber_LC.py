class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # BCA - 2*26*26 + 3*26 + 2 = 1432
        result = 0;
        for x in range(len(columnTitle)):
            result *= 26;
            print(result)
            #ASCII A->65
            result += ord(columnTitle[x]) - 64;
            print(result)
        return result;
        
    x=titleToNumber(1,"ZY")
    print(x)