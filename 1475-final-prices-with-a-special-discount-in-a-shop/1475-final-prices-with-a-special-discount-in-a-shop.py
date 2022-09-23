class Solution:
    def finalPrices(self, prices):
        # lee's solution, much better than me QAQ
        stack = []
        for i, a in enumerate(prices):
            while stack and prices[stack[-1]] >= a:
                prices[stack.pop()] -= a
            stack.append(i)
        return prices