
import numpy as np

def react(polymer):
    check_1, check_2 = 0, 1
    to_remove = set()
    while check_2 < len(polymer):
        # If out of bounds
        if check_1 < 0:
            check_1 = check_2
            check_2 += 1
            continue
        first, second = polymer[check_1], polymer[check_2]
        # If the two characters do not react, iterate forward
        if not is_reactive(first, second):
            check_1 = check_2
            check_2 += 1
        # Else, they do react, so track indices and move outward.
        # The bottom bound must continue moving outward until reaching
        # an index that has not been removed yet.
        else:
            to_remove.add(check_1)
            to_remove.add(check_2)
            check_1 -= 1
            while check_1 in to_remove:
                check_1 -= 1
            check_2 += 1
    # Concatenate string, removing the correct indices
    removed = [polymer[i] for i in range(len(polymer)) if i not in to_remove]
    return "".join(removed)

def is_reactive(a, b):
    return a != b and a.lower() == b.lower()

if __name__ == "__main__":
    f = open("05.txt", "r")
    polymer = f.read()
    polymer = polymer[:len(polymer) - 1]

    # -- Part 1 --
    reacted = react(polymer)
    print(len(reacted))

    # -- Part 2 --
    units = set(polymer.lower())
    min_len = len(polymer)
    for char in units:
        filtered = polymer.replace(char, "").replace(char.upper(), "")
        min_len = min(min_len, len(react(filtered)))
    print(min_len)
