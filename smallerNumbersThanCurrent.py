class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_number=sorted(nums)
        smaller=[]
        counter={}
        for i,num in enumerate(sorted_number):
            if num not in counter:
                counter[num]=i
        for num in nums:
            smaller.append(counter[num])
        return smaller
        
