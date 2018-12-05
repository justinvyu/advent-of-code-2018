
import numpy as np

def react(polymer):
    num_reactions = 0
    check_1, check_2 = 0, 1
    lower_bound = 0
    to_remove = set()
    while check_2 < len(polymer):
        if check_1 < 0:
            check_1 = check_2
            check_2 += 1
            continue
        first, second = polymer[check_1], polymer[check_2]
        if not is_reactive(first, second):
            check_1 = check_2
            check_2 += 1
        else:
            num_reactions += 1
            to_remove.add(check_1)
            to_remove.add(check_2)
            check_1 -= 1
            while check_1 in to_remove:
                check_1 -= 1
            check_2 += 1
    removed = [polymer[i] for i in range(len(polymer)) if i not in to_remove]
    return "".join(removed), num_reactions

def is_reactive(a, b):
    return a != b and a.lower() == b.lower()

def fully_react(polymer):
    polymer, num_reactions = react(polymer)
    while num_reactions:
        prev = str(polymer)
        polymer, num_reactions = react(polymer)
    return polymer

if __name__ == "__main__":
    f = open("05.txt", "r")
    polymer = f.read()
    polymer = polymer[:len(polymer) - 1]

    reacted = fully_react(polymer)
    print(len(reacted))

    units = set(polymer.lower())
    min_len = len(polymer)
    for char in units:
        filtered = "".join(c for c in polymer if c.lower() != char)
        min_len = min(min_len, len(fully_react(filtered)))
    print(min_len)
