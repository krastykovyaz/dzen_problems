# Вход: [1, 3] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]

from typing import List

def merge(seq)->int:
    collector = []
    for val in seq:
        if any(collector):
            f = False
            for col in collector:
                if col[0] < val[0] and col[1] > val[0]:
                    col[1] = val[1]
                    f = True
                if col[0] > val[0] and col[1] < val[1]:
                    col[0] = val[0]
                    f = True
            if f == False:
                collector.append(val)
            f = False
        else:
            collector.append(val)
    return collector

if __name__=='__main__':
    intervals = [[1, 3], [100, 200], [2, 4]]
    print(merge(intervals))