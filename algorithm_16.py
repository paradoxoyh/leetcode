class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
#先排序，第i次循环第一个从第i个开始，第二个从i+1开始，第三个从-1向左，根据正负来决定移动第二个向右或者第三个向左，每次循环找到第i个为第一个数时的最大组合，n次中取最大