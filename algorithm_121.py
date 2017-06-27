class Solution(object):
    def maxProfit(self, prices):
        max = 0
        last = 0
        for i in range(len(prices)):
            if prices[i]-prices[last]>max:
                max=prices[i]-prices[last]
            elif prices[i]<prices[last]:
                last=i
        return max
        """
        :type prices: List[int]
        :rtype: int
        """
        