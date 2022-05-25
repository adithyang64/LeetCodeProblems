class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        list1=[]
        ColumnName=""
        while(columnNumber):
            reminder = (columnNumber-1)%26
            columnNumber=(columnNumber-1)/26
            #ASCII A->65
            list1.append(chr(reminder+65))
        list1.reverse()
        return(ColumnName.join(list1))

    x = convertToTitle(1,7)
    print(x)

    # https://leetcode.com/problems/excel-sheet-column-title/