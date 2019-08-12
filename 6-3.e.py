import math


def tableau_sort(tableau):
    sorted = []
    for i in range(0, int(math.pow(len(tableau), 2))):
        sorted.append(extract_min(tableau))
    return sorted


def extract_min(tableau):
    value = tableau[0][0]
    tableau[0][0] = math.inf
    tableau_heapify(tableau, 0, 0)
    return value


def tableau_heapify(tableau, i, j):
    n = len(tableau)
    m = len(tableau[0])
    smallest_i, smallest_j = i, j
    right_i, right_j = i, j + 1
    bottom_i, bottom_j = i + 1, j

    if right_j < m and tableau[smallest_i][smallest_j] > tableau[right_i][right_j]:
        smallest_i, smallest_j = right_i, right_j
    if bottom_i < n and tableau[smallest_i][smallest_j] > tableau[bottom_i][bottom_j]:
        smallest_i, smallest_j = bottom_i, bottom_j
    if smallest_i != i or smallest_j != j:
        tableau[i][j], tableau[smallest_i][smallest_j] = tableau[smallest_i][smallest_j], tableau[i][j]
        tableau_heapify(tableau, smallest_i, smallest_j)


tableau0 = [
    [2, 3, 4, 9],
    [5, 6, 8, 11],
    [16, 17, 20, 88],
    [21, 22, 77, 99]
]

print(tableau_sort(tableau0))
