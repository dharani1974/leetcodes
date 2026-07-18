class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        # st=str(num)
        # for i in range (0,len(st)):
        #     if num%int(st[i])==0:
        #         count+=1
        # return count
        num2=num
        while num2>0:
            div=num2%10
            num2=num2//10
            if num%div==0:
                count+=1
        return count