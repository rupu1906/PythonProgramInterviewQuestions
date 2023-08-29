# Print even number from 1 to 20 in using one statement
# And then using lambda function

print(*(i for i in range(1,21) if i%2==0))

print(*(i for i in range(2,21,2)))

l= lambda x: x%2==0
print(*(filter(l,range(1,21))))