class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr1=[]
        counted=Counter(arr1)
        for i in arr2:
            for j,k in enumerate(arr1):
                if i == k:
                    h=arr1[j]
                    new_arr1.append(h)
        remainder=sorted(set(arr1)-set(arr2))
        for i in remainder:
            new_arr1 += [i] * counted[i]
        return new_arr1  
        
