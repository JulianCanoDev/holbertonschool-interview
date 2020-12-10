#!/usr/bin/python3
"""
Boxes
"""


def join(T, R):
    """
    Join
    """
    res = []
    for e in R:
        res += T[e]
    return res


def canUnlockAll(boxes):
    """
    Unlock
    """
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True

    return len(total) == len(boxes)
