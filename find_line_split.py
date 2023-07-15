# Дан массив точек с целочисленными координатами (x, y). 
# Определить, существует ли вертикальная прямая, делящая точки на 2 симметричных относительно этой прямой множества. 
# Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}
from typing import Dict, List
from collections import defaultdict

def is_opposite(points: List[Dict[int,int]])-> bool:
    points_dict = defaultdict(list)
    for point in points:
       points_dict[point["x"]].append(point["y"])
    for x in points_dict.keys():
        if -x in points_dict:
            if points_dict[-x] == points_dict[x]:
                return True
    return False


if __name__=='__main__':
    t1 = [{'x': 1, 'y': 2}, {'x': -1, 'y': 2}, {'x': 3, 'y': 4}, {'x': -3, 'y': 4}]
    t2 = [{'x': 1, 'y': 2}, {'x': -2, 'y': 2}, {'x': 3, 'y': 4}, {'x': -5, 'y': 4}]
    print(is_opposite(t1))
    assert is_opposite(t2) == False