def anagram_strings(x,y):
    print(sorted(x),sorted(y))
    f_sorted = ''.join(sorted(x))
    s_sorted = ''.join(sorted(y))
    print(f_sorted, s_sorted)
    if f_sorted == s_sorted:
        print("Strings are anagram")
    else:
        print("String are not anagram string")
        
def anagram_strings(x,y):
    print("Hello")


anagram_strings("acbd", "cdab")
x= "hello"
y = "lloeh"

if sorted(x) == sorted(y):
    print("Strings are anagram String")
else:
    print("String are not anagram string")

str = "Python is a programming language"
print (str.isalnum())
str = "This is Interview Question 17"
print (str.isalnum())

