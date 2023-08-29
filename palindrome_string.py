def palindrom_string(str1):
    l = list(str1)
    reverse_list =l.copy()
    l.reverse() 
    if l == reverse_list:
        print("It's a palindrom string")
    else:
        print("It's not a palindrom string")
palindrom_string("heleh")

def palindrom_string_second(str1):
    reverse_str = str1[::-1]
    if str1 == reverse_str:
        print("It's a palindrom string")
    else:
        print("It's not a palindrom string")
palindrom_string("heleh")