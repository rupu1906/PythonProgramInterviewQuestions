# def swap_two_number(x,y):
#     print(f"Befire swap X = {x} and Y = {y}")
#     temp = x
#     x = y
#     y = temp

#     print(f"After swap X = {x} and Y = {y}")

# swap_two_number(10,5)

# def swap_two_string(x,y):
#     print(f"Befire swap X = {x} and Y = {y}")
#     temp = x
#     x = y
#     y = temp

#     print(f"After swap X = {x} and Y = {y}")

# swap_two_number("hello","rupali")

# def swap_two_numbers_without_third_variable(x,y):
#     print(f"Before swap X = {x} and Y = {y}")
#     x = x +y 
#     y = x -y
#     x = x- y
#     print(f"After swap X = {x} and Y = {y}")

# swap_two_numbers_without_third_variable(10,5)

def swap_two_string_without_third_variable(x,y):
    print(f"Before swap X = {x} and Y = {y}")
    x = x + y 
    y = x[:len(x)-len(y)]
    x =x[len(y):]
    print(f"After swap X = {x} and Y = {y}")

swap_two_string_without_third_variable("Hello","Rupali")

def swap_two_number_with_assignment(x,y):
    print(f"Befire swap X = {x} and Y = {y}")
    x,y = y, x
    print(f"After swap X = {x} and Y = {y}")
swap_two_number_with_assignment(10,5)

def swap_two_string_with_assignment(x,y):
    print(f"Before swap X = {x} and Y = {y}")
    x,y = y, x
    print(f"After swap X = {x} and Y = {y}")

swap_two_string_with_assignment("hello ",'how are you?')