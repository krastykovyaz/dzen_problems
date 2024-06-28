# a = [3,2,4,5,1]
from typing import List

def b_sort(seq: List[int])->List[int]:
    i = 0
    while i < len(seq):
        j = 0
        while j < len(seq):
            if seq[i] < seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
            j += 1
        i += 1


if __name__=='__main__':
    a = [3,2,4,5,1]
    b_sort(a)
    print(a)