import math


def tableau_insert(tableau, value):
    tableau[len(tableau) - 1][len(tableau) - 1] = value
    tableau_heapify_revert(tableau, len(tableau) - 1, len(tableau) - 1)


def tableau_heapify_revert(tableau, i, j):
    highest_i, highest_j = i, j
    left_i, left_j = i, j - 1
    upper_i, upper_j = i - 1, j

    if left_j >= 0 and tableau[highest_i][highest_j] < tableau[left_i][left_j]:
        highest_i, highest_j = left_i, left_j
    if upper_i >= 0 and tableau[highest_i][highest_j] < tableau[upper_i][upper_j]:
        highest_i, highest_j = upper_i, upper_j
    if highest_i != i or highest_j != j:
        tableau[i][j], tableau[highest_i][highest_j] = tableau[highest_i][highest_j], tableau[i][j]
        tableau_heapify_revert(tableau, highest_i, highest_j)


tableau0 = [
    [2, 3, 4, 5],
    [7, 6, 8, 11],
    [16, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf]
]

tableau_insert(tableau0, 1)
print(tableau0)

tableau_insert(tableau0, 9)
print(tableau0)
