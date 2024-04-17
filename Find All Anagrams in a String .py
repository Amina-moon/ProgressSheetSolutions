class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_of_p=len(p)
        length_of_s=len(s)
        index=0
        counter_of_p = Counter(p)
        first_indexes = []
        for i in range(length_of_p,length_of_s + 1):
            if Counter(s[index:i]) == counter_of_p:
                first_indexes.append(index)
                index += 1
            else:
                index += 1
        return first_indexes
        
