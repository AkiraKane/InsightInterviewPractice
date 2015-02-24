class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0

        last_word_ind = None
        current_ind = len(s) - 1
        while (last_word_ind is None):
            if current_ind == 0:
                last_word_ind = 0
            if s[current_ind] == ' ':
                last_word_ind = current_ind + 1
            else:
                current_ind -= 1
        return len(s) - last_word_ind + 1
