# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
# [1, 1, 0]
from typing import List
def get_one_seq(seq:List[int])->int:
    if len(seq) == 1:
        return 1
    i = 1
    maximum = 0
    while i < len(seq):
        count = 0
        f = False
        j = 0
        while count < len(seq) - i:
            if seq[count + i - 1] == 0:
                f = True
                j += 1
            if f and seq[count + i] == 0:
                maximum = max(maximum, count)
                count = 0
                f = False
                i += j
                break
            count+=1
        i += 1
        maximum = max(maximum, count)
    
    return maximum


if __name__=='__main__':
    t1 = [0, 1, 1, 0, 1, 1]
    t2 = [0, 1]
    t3 = [1, 0, 1]
    t4 = [0, 0, 1]
    print(get_one_seq(t2))
    assert get_one_seq(t2) == 2