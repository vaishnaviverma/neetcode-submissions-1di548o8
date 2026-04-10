class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = 101
        ans = -1
        for price in prices:
            least = min(least, price)
            ans = max(ans, price-least)
        return ans

        