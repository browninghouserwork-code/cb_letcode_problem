from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        firstword = strs[0]
        for i in range(1, len(strs)):
            extraword = str[i]
            while firstword:
                if extraword.startswith(firstword):
                    break
                firstword = firstword[1:len(firstword) - 1]
                if firstword == "":
                    return ""
        return firstword
