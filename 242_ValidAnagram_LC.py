class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}   
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False
        for value in dic.values():
            if value != 0:
                return False
        return True
    
    ## if(sorted(t)== sorted(s)):
    ##   return True
    ## else:
    ##   return False

    x = isAnagram(1,"anagram","nagaram")
    print(x)

    # https://leetcode.com/problems/valid-anagram/