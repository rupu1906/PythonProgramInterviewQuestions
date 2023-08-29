# Next number is a sum of prev 2 numbers
def fibonacci_series(x):
    a = 0
    b= 1
    for _ in range(x):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
             

fibonacci_series(3)