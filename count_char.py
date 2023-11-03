def freq_char(string: str) -> str:
    if len(string) == 1:
        return string[0]
    i = 1
    count = 1
    max_freq = 0
    freq_char = None
    while i < len(string):
        if string[i - 1] == string[i]:
            count += 1
            if max_freq < count:
                freq_char = string[i]
                max_freq = count
        else:
            count = 1
        i += 1

    return freq_char


assert freq_char('aabbb') == 'b'
assert freq_char('aaabb') == 'a'
assert freq_char('') == None
assert freq_char('aaaa') == 'a'
assert freq_char('a') == 'a'
assert freq_char('aabb') == 'a'
