class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mm = [] 
        right = len(piles) - 2
        left = 0
        count = 0
        while left < right:
            count += piles[right]
            left += 1
            right -= 2
        return count
