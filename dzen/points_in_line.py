# принадлежат ли точки одной прямой
# points = [[1, 2], [3, 4], [1, 2], [3, 4], [5, 6]]
from typing import List
from collections import defaultdict

def is_in_line(points: List[List[int]])->bool:
    if len(points) == 1:
        return None
    if len(points) == 2:
        return True
    cases = [1,1,1]
    for i in range(1, len(points)):
        first = abs(points[i][0]) - abs(points[i-1][0])
        second = abs(points[i][1]) - abs(points[i-1][1])
        if first == second:
            cases[0]+= 1
        if first == 0:
            cases[1]+= 1
        if second == 0:
            cases[2]+= 1
    return max(cases) == len(points)



if __name__=='__main__':
    assert is_in_line([[1, 2], [3, 4], [1, 2], [3, 4], [5, 6], [-1, -2]]) == True
    assert is_in_line([[-2, -1], [-1, -1], [1, 1]]) == True
    assert is_in_line([[1, 2], [1, 4], [1, 2], [1, 3]]) == True
    assert is_in_line([[1, 2], [-1, 4], [1, 2]]) == True
    assert is_in_line([[1, 2]]) == None
    assert is_in_line([[1, 2], [3, 4], [1, 2]]) == True
    assert is_in_line([[1, 2], [1, 4], [-1, 6], [1, 3]]) == True
    assert is_in_line([[1, 1], [2, 2], [33, 33]]) == True

