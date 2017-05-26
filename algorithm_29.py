class Solution(object):
    def divide(self, dividend, divisor):
        isPositive=(dividend>=0)^(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        result=0
        while dividend >= divisor:
            n,nb=1,divisor
            while dividend>=nb:
                dividend,result=dividend-nb,result+n
                n,nb=n<<1,nb<<1
        return min(result,2147483647) if isPositive else max(-result,-2147483648)
        #<<操作符表示二进制中的右移操作，右移1位变成2倍，两位变成4倍
