# Даны даты заезда и отъезда каждого гостя. Для каждого гостя дата заезда строго раньше даты отъезда (то есть каждый гость останавливается хотя бы на одну ночь). В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые. Найти максимальное число постояльцев, которые одновременно проживали в гостинице (считаем, что измерение количества постояльцев происходит в конце дня).

# sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]
from typing import List, Tuple
from collections import defaultdict

def get_intersections(seq: List[Tuple[int, int]])->int:
    arrive = defaultdict(int)
    depart = defaultdict(int)
    for s in seq:
        arrive[s[0]] += 1
        depart[s[1]] += 1
    res = 0
    current = 0

    for day in sorted(set(arrive.keys()).union(set(depart.keys()))):
        current -= depart[day]
        current += arrive[day]
        res = max(res, current)
    return res

    

if __name__=='__main__':
    t1 = [(1,2), (2,3), (1,4), (3,4)]
    t2 = [(1,4),(1,3), (1,2)]
    t3 = [(1,2), (3,4)]
    sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]
    print(get_intersections(t1))
    assert get_intersections(sample) == 3
