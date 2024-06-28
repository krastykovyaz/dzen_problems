# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def rle(inpt: str)->str:
    if len(inpt) == 0:
        return None
    if len(inpt) == 1:
        return inpt[0]
    i = 1
    collector = [inpt[0]]
    count = 1
    while i < len(inpt):
        if inpt[i - 1] == inpt[i]:
            count += 1
        else:
            if count > 1:
                collector.append(str(count))
            count = 1
            collector.append(inpt[i])
        i += 1
    if count > 1:
        collector.append(str(count))
    return ''.join(collector)

if __name__=='__main__':
    string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'

    print(rle(string))
    assert rle(string)=='A4B3C2XYZD4E3F3A6B28'
    assert 'A' == rle('A')
    assert 'ABC' == rle('ABC')

