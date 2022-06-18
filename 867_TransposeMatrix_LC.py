class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows=(len(matrix))
        num_cols=(len(matrix[0]))
        ans = [[None] * num_rows for _ in range(num_cols)]
        for i in range(num_rows):
            for j in range(num_cols):
                ans[i][j]=matrix[j][i]
        return ans
    
    ans = transpose(1,[[1,2,3],[4,5,6],[7,8,9]])
    print(ans)

# https://leetcode.com/problems/transpose-matrix/