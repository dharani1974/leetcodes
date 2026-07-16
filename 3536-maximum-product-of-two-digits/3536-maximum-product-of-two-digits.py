class Solution:
    def maxProduct(self, n: int) -> int:
        d1=float("-inf")
        d2=float("-inf")
        for char in str(n):
            digit=int(char)
            if digit>=d1:
                d2=d1
                d1=digit
            elif digit>d2:
                d2=digit
        return(d1*d2)
