def looking_range(seq, target):
    sort_seq = sorted(seq)
    right = 0
    left = 0
    mem = sort_seq[0]
    while right < len(sort_seq):
        if mem == target:
            return range(left - 1, right)
        elif mem < target:
            right += 1
            if right < len(sort_seq):
                mem += sort_seq[right]
        else:
            mem -= sort_seq[left]
            left += 1
        

if __name__=='__main__':
    t1 = [1, -3, 4, 5]
    target = 9
    target2 = 2
    target3 = -2
    elements = [5, 10, 15, 20]
    target = 25
    elements = [1, 2, 3, 4]
    target = 100
    elements = [1, -1, 1, -1, 1]
    target = 0

    print(looking_range(elements, target))