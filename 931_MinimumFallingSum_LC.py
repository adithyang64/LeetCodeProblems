class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Top Down Approach
        #print(len(matrix))
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                # Left Edge Elements
                if(j==0):
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                # Right Edge Elements
                elif(j==len(matrix)-1):
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j]) 
                # Other Elements
                else:
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
        return min(matrix[len(matrix) - 1])
    
    ans = minFallingPathSum(1,[[2,1,3],[6,5,4],[7,8,9]])
    print(ans)
                  
    # 2 1 3
    # 6 5 4
    # 7 8 9

    # https://leetcode.com/problems/minimum-falling-path-sum/