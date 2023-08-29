class Factorial:
    @staticmethod
    def factorial_recurssion(num):
        if num >1:
            return num * Factorial.factorial_recurssion(num -1)       
        else:
            return 1
    @staticmethod
    def fibonnaci_series_recurssion(num):
        a = 0
        b = 1
        for _ in range(num):
            print(a, end=" ")
            c = a +b
            a = b
            b = c
        
print(Factorial.factorial_recurssion(6))  
Factorial.fibonnaci_series_recurssion(10)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
print()
print("###############")
def fibo(rang):
    a=0
    b=1
    c=1
    for _ in range(rang):
        print(a, end=" ")
        a=b
        b=c
        c=a+b
fibo(10)
print()
print("###############")
def fact_recursive(num):
    if num>1:
        return num * fact_recursive(num-1)
    else:
        return 1
print(fact_recursive(6))