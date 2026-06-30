class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=b=c=None
        for i in nums:
            if a==None:
                a=i
            elif i>a:
                c=b
                b=a
                a=i
            elif i==a:
                continue
            elif b==None:
                b=i
            elif i>b:
                c=b
                b=i
            elif i==b:
                continue
            elif c==None:
                c=i
            elif i>c:
                c=i
        return c if c!=None else a
