class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s=0
        for char in columnTitle:
            s=s*26+(ord(char)-ord("A")+1)
        return s