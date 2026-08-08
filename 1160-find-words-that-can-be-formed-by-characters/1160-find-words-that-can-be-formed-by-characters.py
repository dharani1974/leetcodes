class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        seen={}
        res=0
        for i in chars:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for word in words:
            tempdic=seen.copy()
            tempres=0
            for char in word:
                if char in tempdic and tempdic[char]>0:
                    tempdic[char]-=1
                    tempres+=1
                    if len(word)==tempres:
                        # seen=tempdic
                        res+=tempres
                else:
                    break
        return res