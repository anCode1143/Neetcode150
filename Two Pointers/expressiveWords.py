from itertools import groupby
from typing import List

def expressiveWords(self, s: str, words: List[str]) -> int:
    def group_chars(s):
        return [''.join(g) for _, g in groupby(s)]
    def is_stretchy(s_list, word_list):
        if len(word_list) != len(s_list):
            return False
        for group_index in range(len(s_list)):
            if not (s_list[group_index][0] == word_list[group_index][0] and len(s_list[group_index]) >= len(word_list[group_index])
                and (len(s_list[group_index]) > 2 or s_list[group_index] == word_list[group_index])):
                return False
        return True
            
    answer = 0
    s_list = group_chars(s)
    for word in words:
        word_list = group_chars(word)
        if is_stretchy(s_list, word_list):
            answer += 1
    return answer