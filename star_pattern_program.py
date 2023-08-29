"""
*
* *
* * *
"""

# def print_star(row_num):
#     for i in range(1, row_num+1):
#         for _ in range(i):
#             print("*", end= " ")
#         print("\n")
# print_star(3)
"""
   * * * 
   * *
   *
"""
# def print_star(row_num):
#     for i in range(row_num,0,-1):
#         for _ in range(i):
#             print("*", end= " ")
#         print("\n")
# print_star(3)

"""
   * * * 
   * *
   *
"""
def print_pyramid_star(row_num):
    for i in range(1, row_num + 1): #3
        for j in range(row_num -i): # 2
            print(" ", end= " ")
        for _ in range(2*i-1):
            print("*", end= " ")
        print("\n")
print_pyramid_star(9)
