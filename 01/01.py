
f = open("01.txt", "r")

input_txt = f.readlines()
assert input_txt, "Error: empty input text"

# Need logn search time, or else it will take forever
prev_totals = set()

def find_total(lines, total=0):
    found = False
    for line in lines:
        if line[0] == '-':
            total -= int(line[1:])
        else:
            total += int(line[1:])
        if total not in prev_totals:
            prev_totals.add(total)
        else:
            found = True
            return total, found
    return total, found

total, found = find_total(input_txt)
while not found:
    total, found = find_total(input_txt, total)

print(total)
