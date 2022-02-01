def bubble_sort(l):
    """
    バブルソート (n-1)(n-2)...n^2/2 計算量はO(n^2)
    https://www.codereading.com/algo_and_ds/algo/bubble_sort.html
    隣り合う要素を比較し入れ替える
    """
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            print(f"i:{i} j:{j}")
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
                print(l)
    print(l)
