class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = list(s.split())
    
        # rtype=0
        # s = s.strip()
        # for i in range(len(s)-1,-1,-1):
        #     if(s[i]==" "):
        #         break
        #     else:
        #         rtype=rtype+1
        
        return len(a[-1])
    
    x=lengthOfLastWord(1,"Hello World    ")
    print(x)

    # https://leetcode.com/problems/length-of-last-word/
            

        