def does_tableau_contain(tableau, n):
    j = 0
    i = len(tableau) - 1
    while j < len(tableau[0]) and i >= 0:
        if tableau[i][j] == n:
            return True
        elif tableau[i][j] < n:
            j += 1
        else:
            i -= 1
    return False


tableau0 = [
    [2, 3, 4, 9],
    [5, 6, 8, 11],
    [16, 17, 20, 88],
    [21, 22, 77, 99]
]

print(does_tableau_contain(tableau0, 8))  # expected: True
print(does_tableau_contain(tableau0, 12))  # expected: False
print(does_tableau_contain(tableau0, 99))  # expected: True
