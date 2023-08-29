def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))

def total_fruits(**kwarg):
    print(kwarg, type(kwarg))


total_fruits(banana=5, mango=7, apple=8)

def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        
        total += amount
    return total


print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))