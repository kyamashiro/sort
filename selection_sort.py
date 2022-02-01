def selection_sort(l):
    """
    選択ソート 計算量はバブルソートと同じO(n^2)
    最小値を見つけ出し左端へ移動させる
    """
    for i in range(len(l)):
        min = i
        for j in range(i + 1, len(l)):
            if l[min] > l[j]:
                min = j
        # 左端と最小値の値を入れ替え
        tmp = l[i]
        l[i] = l[min]
        l[min] = tmp
        print(l)
