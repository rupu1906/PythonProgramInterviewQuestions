def number_of_string(str):
    l = str.split()
    print(" number of words in a string", len(l))

number_of_string("   Hello how are you? I'm running out of ideas")

def number_of_string_method2(str):
    count = 0
    for i in range(len(str)):
        if str[i] ==" ":
            count += 1 
    print(" number of words in a string", count)
number_of_string("   how   are you? I'm running out of ideas")
