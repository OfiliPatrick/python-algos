#map the sorted version of each string to the input string

#TC: O(nmlogm)
def groupAnagrams(words):
    import collections

    word_dict = collections.defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        word_dict[sorted_word].append(word)

    output = [ word for word in word_dict.values() if len(word) >=2]

    print(word_dict)
    print(output)




print(groupAnagrams(['debitcard', 'elvis', 'silent', 'badcredit', 'lives','freedom']))