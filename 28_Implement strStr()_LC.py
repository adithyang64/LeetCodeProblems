class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(len(needle)>0):
            rtype=haystack.find(needle)
        else:
            rtype=0
        print(rtype)
        return rtype

    x = strStr(1,"hello","ll")

    # https://leetcode.com/problems/implement-strstr/