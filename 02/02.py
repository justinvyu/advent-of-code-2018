import collections, numpy as np

def count_letter_occurences(box_id):
    """
    Returns a hashmap of the each character to the frequency of the
    character in the word. The order of the characters in the dictionary
    does not matter.

    >>> count_letter_occurences("abcdef")
    {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
    >>> count_letter_occurences("bababc")
    {'b': 3, 'a': 2, 'c': 1}
    """
    return collections.Counter(box_id)

def diff_letters(word1, word2):
    """
    Returns the difference of two words as a list with the difference of
    the ASCII value of the characters of word1 with the ASCII value of the
    characters of word2.

    >>> diff_letters("abcde", "abcde")
    [0, 0, 0, 0, 0]
    """
    return [ord(a) - ord(b) for a, b in zip(list(word1), list(word2))]

if __name__ == "__main__":
    f = open("02.txt", "r")
    ids = f.readlines()

    # -- Part 1 --

    two_count, three_count = 0, 0
    for box_id in ids:
        freqs = count_letter_occurences(box_id).values()
        if 2 in freqs:
            two_count += 1
        if 3 in freqs:
            three_count += 1

    checksum = two_count * three_count
    print(checksum)

    # -- Part 2 --

    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            diff = set(diff_letters(ids[i], ids[j]))
            if len(diff) == 2 and 0 in diff:
                print(ids[i], ids[j])
                diff_index = np.argmax(diff_letters(ids[i], ids[j]))
                print(ids[i][:diff_index] + ids[i][diff_index + 1:])
                break

