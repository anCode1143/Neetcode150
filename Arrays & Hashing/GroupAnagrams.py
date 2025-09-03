def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    words_map = {}
    for words in strs:
        if not "".join(sorted(words)) in words_map:
            words_map["".join(sorted(words))] = []
            words_map["".join(sorted(words))].append(words)
        else:
            words_map["".join(sorted(words))].append(words)
            
    answer = words_map.values()
    return answer

print(groupAnagrams(["eat", "eat", "tan", "ate", "nat", "bat"]))