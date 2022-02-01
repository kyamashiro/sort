def insertion_sort(l):
    """
    挿入ソート (n-1)(n-2)... O(n^2)
    """
    for i in range(len(l)):
        min = None
        for j in range(i, -1, -1):
            print(f"i:{i} j:{j}")
            print(f"{l[i]} < {l[j]}")
            if l[i] < l[j]:
                min = j
        print(f"min:{min}")
        if min is not None:
            l.insert(min, l.pop(i))
        print(l)
