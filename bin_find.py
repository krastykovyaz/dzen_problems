# найти индекс элемента в отсортированном списке элементов
from typing import List


def b_serch_idx(seq: List[int], target: int) -> int:
    if len(seq) > 0 and target in seq:
        def b_search(s, start, end, target):
            mid = ((end - start) // 2) + start
            if s[mid] == target:
                return mid
            if s[mid] > target:
                return b_search(s, start, mid, target)
            else:
                return b_search(s, mid, end, target)
        return b_search(seq, 0, len(seq), target)
    else:
        return -1


if __name__ == '__main__':
    seq = [1, 3, 10, 23, 56, 101]
    target = 101
    print(b_serch_idx(seq, target))
    t1 = [2,4]
    assert b_serch_idx(t1, 2) == 0
