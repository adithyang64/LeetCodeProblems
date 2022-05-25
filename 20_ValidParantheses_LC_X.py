class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rtype=False
        if(len(s)>1):
            if(s[0]== ')' or s[0]=='}' or s[0]==']'):
                    if(s[0]!= '(' and s[0]!='{' and s[0]!='['):
                        print(rtype)
                        return rtype
            stack=[]
            for i in s:
                if(i== '(' or i=='{' or i=='['):
                    stack.append(s[0])
                    if(len(stack)):
                        if(i== ')' and stack[-1]=='('):
                            stack.pop()
                        elif(i== ']' and stack[-1]=='['):
                            stack.pop()
                        elif(i== '}' and stack[-1]=='{'):
                            stack.pop()
            if(len(stack)==0):
                rtype= True
        print(rtype)
        return rtype
    
    rtype1=isValid(1,"()")

    # https://leetcode.com/problems/valid-parentheses/