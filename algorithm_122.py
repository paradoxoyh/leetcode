class Solution(object):
    def maxProfit(self, prices):
        sum = 0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                sum +=prices[i+1]-prices[i]
        return sum
        """
        :type prices: List[int]
        :rtype: int
        """
        