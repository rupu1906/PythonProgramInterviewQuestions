#Natural number, greater than 1, which can be divided by 1 and itself
def prime_number(x):
    if x == 1:
        print("Prime number")
    else:
        for i in range(2, x//2+1):
            if x%i == 0:
                print(f"{x} is not a prime number")
                break
        else:
            print(f"{x} is a prime Number")
# prime_number(7)

def prime_all_prime_numbers(x):
    if x == 1:
        print(" ")
    else:
        for i in range(2,x+1):
            for j in range(2,(i//2)+1):
                if i%j == 0:
                    break
            else:
                print(i, end=" ")

prime_number(20)
prime_number(4)
prime_all_prime_numbers(20)
print()

def prime_all_prime_numbers_using_decorator(func):
    def wrapper(num):
        list =[]
        for i in range(2,num):
            if(func(i)):
                list.append(i)
            # prime_number(i)
        print(list)
    return wrapper

@prime_all_prime_numbers_using_decorator
def deco(i):
    for j in range(2,i//2+1):
        if i%j == 0:
            break
    else:
        return True
    return False

l =deco(20)

t = 1,26,3,7,2

list =["Heyy","How","are","you"]
list.reverse()
print(list)

d =dict()
d ={1:"name", 2:"age"}

d.update({"sal":150})
d["a"]="hello"
print(d)

st = "hello how are you? how are you"

print(st.index("how"))
