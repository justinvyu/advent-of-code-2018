import numpy as np
from collections import Counter

def create_grid(xs, ys, offset=0):
    max_x, max_y = max(xs) + 2 * offset, max(ys) + 2 * offset
    return np.full((max_y + 1, max_x + 1), ".", dtype=object)

def closest(x, y, coord_xs, coord_ys):
    dist_to_coords = [abs(x_i - x) + abs(y_i - y) for x_i, y_i in zip(coord_xs, coord_ys)]
    min_val, min_index = min(dist_to_coords), np.argmin(dist_to_coords)
    dist_to_coords.pop(min_index)
    if min_val in set(dist_to_coords):
        return "."
    return min_index

def total(x, y, coord_xs, coord_ys):
    dist_to_coords = [abs(x_i - x) + abs(y_i - y) for x_i, y_i in zip(coord_xs, coord_ys)]
    return sum(dist_to_coords)

def find_areas(coords, offset=0):
    xs, ys = coords[:, 0], coords[:, 1]
    xs, ys = np.array([x + offset for x in xs]), np.array([y + offset for y in ys])
    grid = create_grid(xs, ys, offset)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = str(closest(x, y, xs, ys))
    c = Counter([i for j in grid for i in j])
    freqs = []
    for i in range(len(coords)):
        freqs.append(c[str(i)])
    return grid, np.array(freqs)

if __name__ == "__main__":
    f = open("06.txt", "r")
    coords_txt = f.read().splitlines()
    coords = np.array([[int(coord.split(",")[0]),
                        int(coord.split(",")[1])] for coord in coords_txt])

    # -- Part 1 --
    grid, freqs = find_areas(coords)
    expand_grid, compare_freqs = find_areas(coords, 50)
    freqs = freqs[freqs - compare_freqs == 0]
    print(max(freqs))

    # -- Part 2 --
     xs, ys = coords[:, 0], coords[:, 1]
    grid = create_grid(xs, ys)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = total(x, y, xs, ys)
    dists = np.array([i for j in grid for i in j])
    print(len(dists[dists < 10000]))
