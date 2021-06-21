#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins.
"""


def _change_matrix(coin_set, change_amount):
    """Function to create the matrix we'll use for the optimization."""
    matrix = [[0 for m in range(change_amount + 1)] for m in range(len(coin_set) + 1)]
    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix

def makeChange(coins, total):
    """Given a pile of coins of different values."""
    if total == 0:
        return 0

    matrix = _change_matrix(coins, total)
    for c in range(1, len(coins) + 1):
        for r in range(1, total + 1):

            if coins[c-1] == r:
                matrix[c][r] = 1

            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]

            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])

    return matrix[-1][-1]
