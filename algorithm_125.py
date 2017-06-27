class Solution(object):
    def isPalindrome(self, s):
        import re
        ree=re.compile('\w')
        s=s.upper()
        res=ree.findall(s)
        while len(res)>1:
            if res[0]==res[-1]:
                res.pop(0)
                res.pop()
            else:
                return False
                break
        return True
        """
        :type s: str
        :rtype: bool
        """
        #beat 0.21%...

class Solution(object):
    def isPalindrome(self, s):
        import re
        ree=re.compile('\w')
        s=s.upper()
        res_pos=ree.findall(s)
        res_nag=res_pos[::-1]
        return res_nag==res_pos
        """
        :type s: str
        :rtype: bool
        """
        #beat 96%,lol