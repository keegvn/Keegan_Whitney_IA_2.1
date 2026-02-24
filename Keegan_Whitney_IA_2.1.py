# Problem 2

p = int(input("Enter # of packages to ship: "))
s = input("Enter r for regular, e for express: ")

# calculate cost for regular shipping
if s == "r":
    cost = p * 10
    print("Total cost: $", cost)

# calcuate cost for express shipping
if s == "e":
    cost = p * 15
    print("Total cost: $", cost)