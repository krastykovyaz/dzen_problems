# Дан список целых чисел, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, 
# сворачивая соседние по числовому ряду числа в диапазоны.

# Примеры:
# - [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
# - [1, 4, 3, 2] => "1-4"
# - [1, 4] => "1,4"
from typing import List

def get_merge(lst_input: List[int])-> str:
    if len(lst_input) == 1:
        return str(lst_input[0])
    sorted_lst = sorted(lst_input)
    collector = [str(sorted_lst[0])]
    is_end = False
    i = 1
    while i < len(sorted_lst):
        if sorted_lst[i] - sorted_lst[i - 1] == 1:
            is_end = True
        else:
            if collector[-1] != str(sorted_lst[i - 1]):
                collector[-1] += '-'
                collector[-1] += str(sorted_lst[i - 1])
            collector.append(str(sorted_lst[i]))
            is_end = False
        i += 1
    if is_end:
        collector[-1] += '-'
        collector[-1] += str(sorted_lst[i - 1])
    return ','.join(collector)

if __name__=='__main__':
    lst = [1, 4, 5, 2, 3, 9, 8, 11, 0]
    print(get_merge(lst))
    assert get_merge([1, 4, 5, 2, 3, 9, 8, 11, 0]) == "0-5,8-9,11"
    assert get_merge([1, 4, 3, 2]) == "1-4"
    assert get_merge([1, 4, 5, 2, 3, 9, 8, 11, 0]) == "0-5,8-9,11"
    assert get_merge([1, 4]) == "1,4"
    assert get_merge([1]) == "1"