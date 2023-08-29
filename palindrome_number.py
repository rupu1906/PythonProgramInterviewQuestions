# Palindrome is a number which remains same when reversed
def palindrome_number(x):
    reversed_number = str(x)[::-1]
    if x == int(reversed_number):
        print(" It's a palindrome number")
    else:
        print("No, it's not a palindrome number")

palindrome_number(16461)
palindrome_number(151)
palindrome_number(152)
#################################
def palindrome_number_second_method(x):
    temp = x
    rev = 0
    while x > 0:
        num = x % 10
        rev = (rev * 10) + num
        x = x//10

    if temp == rev:
        print(" It's a palindrome number")
    else:
        print("No, it's not a palindrome number")
        
palindrome_number_second_method(121)
