class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add=0
        mul=1
        while n>0:
            dig=n%10
            n=n//10
            add+=dig
            mul=mul*dig
        return mul-add