class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = len(strs[0])
        for i in strs:
            min_len = min(min_len,len(i))
        print(min_len)
        a = ""
        for i in range(min_len):
            x=strs[0][i]
            for j in range(len(strs)):
                if(x!=strs[j][i]):
                    return a
            a += x
            print(a)
        return a

    x = longestCommonPrefix(1,["flower","flow","flight"])

    # https://leetcode.com/problems/longest-common-prefix/