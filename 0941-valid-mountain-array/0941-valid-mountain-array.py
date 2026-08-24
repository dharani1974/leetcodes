class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        mid=0
        for i in range(1,len(arr)):
            if mid==0:
                if arr[i-1]==arr[i]:
                    return False
                elif (arr[i-1]>arr[i]):
                    if i-1!=0:
                        mid+=1
                    else:
                        return False
            else:
                if arr[i-1]==arr[i]:
                    return False
                elif (arr[i-1]<arr[i]):
                    return False
        if mid==0:
            return False
        return True