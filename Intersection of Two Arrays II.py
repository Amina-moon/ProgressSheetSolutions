class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_counter=Counter(nums1)
        num2_counter=Counter(nums2)
        intersection = []
        for i in num1_counter.keys():
            if i in num2_counter:
                occurance=min(num1_counter[i],num2_counter[i])
                intersection += [i] * occurance
        return intersection



        
