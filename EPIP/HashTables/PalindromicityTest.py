def palindromicityTest(s):

    import collections
    char_cnt = collections.defaultdict(int)

    for char in s:
        char_cnt[char] += 1

    for char in char_cnt:
        if char_cnt[char] % 2 != 0 and char_cnt[char] > 1:
            return False
    return True
    

print(palindromicityTest('edified'))