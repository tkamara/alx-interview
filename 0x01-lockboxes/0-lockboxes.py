#!/usr/bin/python3
"""
determining if lockboxes can be opened
"""


def canUnlockAll(boxes):
    """
    determines whether all boxes can be opened
    """
    if type(boxes) is not list or not boxes:
        return False

    checked  = [0]
    for i in checked:
        for key in boxes[i]:
            if key not in checked  and key < len(boxes):
                checked.append(key)

    return len(checked) == len(boxes)
