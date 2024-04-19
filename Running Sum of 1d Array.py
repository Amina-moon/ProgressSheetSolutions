class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer=[]
        counter=0
        for i in range(len(nums)):
            counter+=nums[i]
            answer.append(counter)
        return answer
