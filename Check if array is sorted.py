class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        left,right=0,1
        answer=True
        while right < n:
            if arr[left] <= arr[right]:
                left+=1
                right+=1
            else:
                answer=False
                break
        if answer == True:
            return 1
        else:
            return 0
