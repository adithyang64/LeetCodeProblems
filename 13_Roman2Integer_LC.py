class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        print(len(s))
        a = d[s[len(s) - 1]]
        #print(a)
        # Loop for each character from right to left
        for i in range(len(s)- 2, -1, -1):
        # Check if the character at right of current character is bigger or smaller
            if d[s[i]] >= d[s[i + 1]]:
                a += d[s[i]]
            else:
                a -= d[s[i]]
        print(a)
        return(a)

    x=romanToInt(1,"MCMXCIV")

    # https://leetcode.com/problems/roman-to-integer/


    