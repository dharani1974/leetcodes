class Solution:
    def sortSentence(self, s: str) -> str:
        arr=s.split()
        res=[""]*len(arr)
        for word in arr:
            res[int(word[-1])-1]=word[:-1]
        return " ".join(res) 