def remove_char_from_string(s, char):
    new_string =s.replace(char,"")
    print(new_string)


remove_char_from_string("hello how are you","o")

def remove_char_from_a_index_given_string(s, index):
    new_string =""
    for i in range(len(s)):
        if i != index:
            new_string += s[i]
    print(new_string)

remove_char_from_a_index_given_string("ABCD",2) 


