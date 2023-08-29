#Write following patter
'''
1
1 2
1 2 3
1 2 3 4
'''
def patter(row_number):
    for i in range(1, row_number+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

patter(5)