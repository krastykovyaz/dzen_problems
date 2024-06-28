
from typing import List

def  merge2(l1: List[int], l2: List[int])->List[int]:
    if len(l1) > len(l2):
        long_ = l1
        short_ = l2
    else:
        long_ = l2
        short_ = l1
    i = 0
    j = 0
    res = []
    while i < len(long_):
        if j < len(short_):
            if short_[j] < long_[i]:
                res.append(short_[j])
                j += 1
            else:
                res.append(long_[i])
                i += 1
        else:
            res.append(long_[i])
            i += 1
    
    return res + short_ if j < len(short_) else res


if __name__=='__main__':
    l1 = [1, 3, 4,7,15]
    l2 = [2,5]
    print(merge2(l1, l2))
    assert merge2(l1, l2) == [1, 2, 3, 4, 5, 7,15]
