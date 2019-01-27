filename = "input-day2.txt"
# filename = "input-day2-test.txt"

def compare_ids(id1, id2):
    different_chars = 0
    for char1, char2 in zip(id1, id2):
        if char1 != char2:
            different_chars +=1
    return different_chars < 2

def find_overlap(id1, id2):
    overlap = ''
    for char1, char2 in zip(id1, id2):
        if char1 == char2:
            overlap += char1
    return overlap

def find_similars():
    file = open(filename, "r")
    ids = []
    for line in file:
        ids.append(line)

    for id1 in ids:
        for id2 in ids:
            # print(id1, line2)
            if id1 == id2:
                continue
            if compare_ids(id1, id2):
                return(id1, id2)
    print(line1)

(id1, id2) = find_similars()

print(id1, id2)
print(find_overlap(id1, id2))