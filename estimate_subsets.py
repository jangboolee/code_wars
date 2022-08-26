from itertools import combinations


def est_subsets(arr):

    unique = set(arr)

    all_combinations = []
    for i in range(len(unique) + 1):
        all_combinations += list(combinations(unique, i))

    return len([comb for comb in all_combinations if len(comb) > 0])
