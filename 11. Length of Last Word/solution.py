class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1  # Skip trailing spaces at the end of the string
        
        while i >= 0 and s[i] != ' ':
            length += 1 # Count characters of the last word
            i -= 1 # Move pointer left through the word

        return length
