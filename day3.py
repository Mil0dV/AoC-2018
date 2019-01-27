filename = "input-day3.txt"

class Claim:
    def __init__(self, id, x_offset, x_size, y_offset, y_size):
        self.id = id
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x_size = x_size
        self.y_size = y_size

    def __str__(self):
        return str(self.__dict__)

def read_claims(filename):
    file = open(filename, "r")
    claims = []
    for line in file:
        elements = line.split()
        id = int(elements[0][1:])
        x_offset = int(elements[2].split(',')[0])
        y_offset = int(elements[2].split(',')[1][:-1])
        x_size, y_size = map(int, elements[3].split('x'))

        claim = Claim(id, x_offset, x_size, y_offset, y_size)
        claims.append(claim)
    return claims

def create_fabric(n):
    x = [0] * n
    for i in range(n):
        x[i] = [0] * n
    return x

def calculate_overlap():
    claims = read_claims(filename)
    fabric = create_fabric(1000)

    for claim in claims:
        # vanaf x_offset +1 * x_size
        for x in range(claim.x_size):
            # print claim.x_offset
            # print i
            # fabric[claim.x_offset + i][claim.y_offset] += 1 
            for y in range(claim.y_size):
                fabric[claim.x_offset + x][claim.y_offset + y] += 1 
        # fabric[claim.x_offset] += 1 * claim.x_size


    # dit kan dus met zoiets:
    # [[int(x) for x in sub] for sub in f]
    # nested list comprehension
    # len([[i if i > 1 for i in sub] for sub in fabric)
    
    # deze werkt _bijna_:
    overlap_squares = len([[i for i in sub if i > 1] for sub in fabric])

    overlap_squares = 0
    for x in range(1000):
        for y in range(1000):
            if fabric[x][y] > 1:
                overlap_squares +=1

    # print fabric

    return overlap_squares, fabric, claims

# print(read_claims(filename)[8])
the_lapped_fab = calculate_overlap()
print(the_lapped_fab[0])

# V calc overlap doen
# voor elke claim checken of ie een vakje > 1 heeft

def find_snowflake_claim(claims, fabric):

    def flake_test(claim):
        for x in range(claim.x_size):
            for y in range(claim.y_size):
                if fabric[claim.x_offset + x][claim.y_offset + y] > 1:
                    return False
        return True

    for claim in claims:
        if flake_test(claim):
            return claim

print find_snowflake_claim(claims = the_lapped_fab[2], fabric = the_lapped_fab[1])