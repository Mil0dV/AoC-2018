filename = "input-day2.txt"
# filename = "input-day2-test.txt"

def calculate_checksum():
    file = open(filename, "r")
    doubles = 0
    triples = 0

    for line in file:
        double_letters = set()
        triple_letters = set()
        for char in line:
            if line.count(char) == 2:
                double_letters.add(char)
            if line.count(char) == 3:
                triple_letters.add(char)

        if len(double_letters) > 0:
            doubles += 1 
        if len(triple_letters) > 0:
            triples += 1

    print(doubles)
    print(triples)
    return(doubles * triples)            

print(calculate_checksum())