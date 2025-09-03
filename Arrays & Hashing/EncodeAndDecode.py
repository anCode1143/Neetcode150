import re

def encode(strs):
    # write your code here
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    answer = ""
    for word in strs:
        delimiter = str(len(word)) + "="
        answer += delimiter + word
    return answer



def decode(str):
    # write your code here
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    answer = []
    for match in re.finditer(r'\d+', str):
        number = int(match.group())           # e.g. '123'
        word_start = match.end()          # index after the number
        if str[word_start] == "=":
            word_start += 1
            word_answer = ""
            for index in range(word_start, word_start+number):
                word_answer += str[index]
            answer.append(word_answer)
            word_answer = ""
    return answer

input = ["peepee", "poopoo", "lol"]
print(encode(input))
print(decode(encode(input)))

input = ["hello", "world"]
print(encode(input))
print(decode(encode(input)))

input = ["", "a", "bc", "def"]
print(encode(input))
print(decode(encode(input)))

input = ["123", "=", "===", "test="]
print(encode(input))
print(decode(encode(input)))

input = ["", "", ""]
print(encode(input))
print(decode(encode(input)))

input = [" ", "  ", "   "]
print(encode(input))
print(decode(encode(input)))

input = ["a"*100, "b"*200]
print(encode(input))
print(decode(encode(input)))