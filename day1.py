filename = "input-day1.txt"
# filename = "input-day-test.txt"

# TODO: deze while loop fixen zodat het zonder functie kan
# while frequency not in reached_frequencies:

def reach_frequency():
    frequency = 0    
    # reached_frequencies = []
    reached_frequencies = set()
    while True: 
        file = open(filename, "r")
        for line in file:
            frequency = frequency + int(line)
            if frequency in reached_frequencies:
                return frequency
            reached_frequencies.add(frequency)
        print(str(frequency) + ", " + str(len(reached_frequencies)))

print(reach_frequency())
