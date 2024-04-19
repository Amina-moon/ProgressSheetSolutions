class NumArray:

    def __init__(self, nums: List[int]):
        self.sumeduplist=[]
        sumedup=0
        for i in nums:
            sumedup += i
            self.sumeduplist.append(sumedup)
        

    def sumRange(self, left: int, right: int) -> int:
        rsum=self.sumeduplist[right]
        lsum=self.sumeduplist[left-1] if left > 0 else 0
        return rsum-lsum

        


