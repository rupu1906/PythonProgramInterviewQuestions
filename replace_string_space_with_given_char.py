def replce_space_with_char(str, char):
    new_str =str.replace(" ",char)
    print(new_str)

replce_space_with_char("hello world!!How's it goin?", "@@")

def replce_space_with_char_without_replace(str, char):
    new_str =""
    for i in range(len(str)):
        if str[i] == " ":
            new_str = new_str + char
        else:
            new_str = new_str + str[i]         
    print(new_str)

replce_space_with_char_without_replace("hello world!!How's it goin?", "##")
