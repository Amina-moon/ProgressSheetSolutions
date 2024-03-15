class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[nums[num % n] for num in range(0,2*n)]
        return ans
