class Solution(object):
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for i in xrange(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = max(candies[i + 1], candies[i] + 1)
            
            j = -i - 1
            if ratings[j - 1] > ratings[j]: 
                candies[j - 1] = max(candies[j - 1], candies[j] + 1)
        return sum(candies)
        """
        :type ratings: List[int]
        :rtype: int
        """
        