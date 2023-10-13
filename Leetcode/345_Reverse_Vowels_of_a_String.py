class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        dic = {}
        lst1 = []
        lst2 = []
        for i, c in enumerate(s):
            if c in vowels:
                dic[i] = 1
                lst1.append(c)
            else:
                dic[i] = 0
                lst2.append(c)

        result = ''
        for key in dic:
            if dic[key] == 1:
                result += lst1.pop()
            else:
                result += lst2.pop(0)

        return result