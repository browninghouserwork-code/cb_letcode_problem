class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        firstword = strs[0] # take the first word as initial prefix
        for i in range(1, len(strs)):
            extraword = strs[i] # compare with next word
            while firstword:
                
                if extraword.startswith(firstword):
                    break # prefix found, move to next word
                firstword = firstword[0:len(firstword) - 1]# Shorten prefix by one character
                if firstword == "":
                    return ""
        
        return firstword # Return the final common prefix