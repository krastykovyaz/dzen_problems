# Даны две строки.

# Написать функцию, которая вернёт True, 
# если из первой строки можно получить вторую, совершив не более 1 изменения (== удаление / замена символа).
def compare_strings(s1: str, s2:str)->bool:
    count = 0
    if len(s2) <= len(s1):
        short_s = s2
        long_s = s1
    else:
        short_s = s1
        long_s = s2
    if abs(len(s1) - len(s2)) == 1:
        i = 1
        while i < len(short_s):
            if short_s[i-1] != long_s[i-1]:
                count += 1
                long_s = long_s[:i-1] + long_s[i:]
                if count > 1:
                    return False
            i += 1
        return True
    elif abs(len(s1) - len(s2)) == 0:
        i = 0
        while i < len(short_s):
            if long_s[i] != short_s[i]:
                count += 1
                if count > 1:
                    return False
            i += 1
        return True
    else:
        return False

if __name__=='__main__':
    s1 = 'abcdef'
    s2 = 'abcdzd'
    print(compare_strings(s1, s2))
