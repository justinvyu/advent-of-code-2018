import numpy as np

def convert_claim_str(claim):
    """
    Returns a tuple of 3 values, parsing from a claim string to give
    the claim number [0], the distance in x-y away from the origin [1],
    and the area of the claim (width, height) [2].

    >>> convert_claim_str("123 @ 3,2: 5x4")
    (123, (3, 2), (5, 4))
    """
    claim = claim.replace(" ", "")
    claim_num, rest = claim[1:].split("@")
    coord, area = rest.split(":")
    x, y = coord.split(",")
    w, h = area.split("x")

    return int(claim_num), (int(x), int(y)), (int(w), int(h))

def apply_claim(claim, arr):
    """
    Performs an operation on the fabric array that parses a claim and
    sets the values of the appropriate indices in the array to the
    claim number.

    >>>
    """
    num, coord, area = claim

    overlaps = 0
    for row in range(coord[1], coord[1] + area[1]):
        for col in range(coord[0], coord[0] + area[0]):
            if arr[row][col] == 0:
                arr[row][col] = 1
            else:
                arr[row][col] = arr[row][col] + 1 # Increment number of overlaps
                overlaps += 1
    if overlaps == 0:
        print("NO OVERLAP!:", num)

    # arr[coord[1]:coord[1]+area[1], coord[0]:coord[0]+area[0]] = num

if __name__ == "__main__":
    f = open("03.txt", "r")
    claims_txt = f.readlines()
    claims_data = [convert_claim_str(claim) for claim in claims_txt]
    claims_data.sort(key=lambda x: x[2][1]+x[2][0])
    print(claims_data)

    size_fabric = 1500
    fabric = np.zeros((size_fabric, size_fabric))

    for claim in claims_data:
        apply_claim(claim, fabric)

    total_area = sum([claim[2][0] * claim[2][1] for claim in claims_data])
    overlap = len(fabric[fabric >= 2]) # Filter for all overlaps that are >= 2
    print("Number of Overlaps:", overlap)
