class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res=[]
        for word in words:
            smallword=word.lower()
            target=smallword[0]
            if target in row1:
                r=row1
            elif target in row2:
                r=row2
            else:
                r=row3
            valid=1
            for char in smallword:
                if char not in r:
                    valid=0
                    break
            if valid==1:
                res.append(word)
        return res