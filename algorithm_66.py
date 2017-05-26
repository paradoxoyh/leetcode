class Solution(object):
    def plusOne(self, digits):
        i = len(digits)-1
        temp = 1
        while i>=0:
            if digits[i]+temp==10:
                digits[i]=0
                i-=1
            else:
                digits[i]+=1
                temp=0
                break
        if temp==1:
            digits.insert(0,1)
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
