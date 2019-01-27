import sys

sys.setrecursionlimit(99999)

filename = "input-day5.txt"
polymer = "dabAcCaCBAcCcaDA"


def collapser(polymer):
    for idx, char in enumerate(polymer):
        # print idx, polymer
        if idx == len(polymer) - 1:
            return polymer
        if polymer[idx + 1] == char.swapcase():
            return collapser(polymer[:idx] + polymer[idx + 2 :])

def read_polymer(filename):
    file = open(filename, "r")
    for polymer in file:
        return polymer

def reduce_polymer(polymer):
    collapsed = collapser(polymer)
    print(collapsed)
    print(len(collapsed))

# huh, off by one?
# reduce_polymer(read_polymer(filename))
# print len(collapser(polymer))


# Part 2
import string
alphabet = string.ascii_lowercase

def improve_polymer(polymer):
    polymer = collapser(polymer)
    shortest_poly = 50000
    for char in alphabet:
        stripped_polymer = filter(lambda ch: ch not in char + char.upper(), polymer)
        collapsed = collapser(stripped_polymer)
        if len(collapsed) < shortest_poly:
            shortest_poly = len(collapsed)
    
    return shortest_poly

# print improve_polymer(polymer)
print improve_polymer(read_polymer(filename))