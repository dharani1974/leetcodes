class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict1 = {}
        word = ""
        i=0
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for ch in key:
            if ch!=' ':
                if ch not in dict1:
                    dict1[ch]=arr[i]
                    i+=1

        for c in message:
            if c==' ':
                word+=' '
            else:
                word += dict1[c]

        return word

