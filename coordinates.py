# Дан массив точек с целочисленными координатами (x, y). 
# Определить, существует ли вертикальная прямая, делящая точки на 2 симметричных относительно этой прямой множества.
# Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}
from typing import Dict, List
from collections import defaultdict

def check_symmetry(points: list[Dict[str, int]])->int:
    delimeter = defaultdict(list)
    for point in points:
        delimeter[point['x']].append(point['y'])
    for k in delimeter.keys():
        if -k in delimeter:
            delimeter[k] == delimeter[-k]
            return True
    return False

    

if __name__=='__main__':
    points = [{'x': 1, 'y': 2}, {'x': -1, 'y': 2}, {'x': 3, 'y': 4}, {'x': -3, 'y': 4}]
    result = check_symmetry(points)
    print(result)
