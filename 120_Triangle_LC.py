class Solution(object):
    def minimumTotal(self, triangle):
        ## Bottom-up Approach
        if triangle: 
            #print(len(triangle))
            #print(triangle[2])
            for i in range(len(triangle)-2, -1, -1):
                for j in range(len(triangle[i])):
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
            return triangle[0][0]
        else:
            return 0

    ans = minimumTotal(1,[[2],[3,4],[6,5,7],[4,1,8,3]])
    print(ans)

    # 2
    # 3 4
    # 6 5 7
    # 4 1 8 7
    
    # https://leetcode.com/problems/triangle/
