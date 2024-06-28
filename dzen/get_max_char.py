from typing import List

def freq_char(s):
    if len(s) == 1:
        return s[0]
    freq_char = None
    max_len = 0
    count = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
            if max_len < count:
                max_len = count
                freq_char = s[i]
        else:
            count = 0
    return freq_char


if __name__=='__main__':
    s1 = 'aaabbb'
    assert freq_char('aabbb') == 'b'
    assert freq_char('aaabb') == 'a'
    assert freq_char('') == None
    assert freq_char('aaaa') == 'a'
    assert freq_char('a') == 'a'
    assert freq_char('aabb') == 'a'