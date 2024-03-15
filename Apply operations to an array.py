class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1] :
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            i += 1
        answer=[num for num in nums if num != 0]
        counter=len(nums) - len(answer)
        for i in range(counter):
            answer.append(0)
        return answer
