from typing import List,Tuple

def merge_intervals(seq: List[Tuple[int, int]])->List[int]:
    sorted_intervals = sorted(seq)
    res = []
    last_interval = None
    for interval in sorted_intervals:
        if not last_interval:
            res = [interval]
            last_interval = interval
            continue
        if last_interval[1] >= interval[0]:
            res[-1][0] =  min(interval[0], last_interval[0])
            res[-1][1] =  max(interval[1], last_interval[1])
            last_interval = res[-1]
        else:
            res.append(interval)
            last_interval = interval
    return res


    
if __name__=='__main__':
    intervals = [[1, 3], [100, 200], [2, 4]]
    t2 = [[1, 100], [100, 200], [2, 4]]
    t3 = [[10, 100], [1, 200]]
    print(merge_intervals(t2))
    assert len(merge_intervals(t3)) == 1