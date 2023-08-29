def remove_string(list_input):
    list2=list()
    for word in list_input:
        if(not isinstance(word, str)):
            list2.append(word)
    list2.sort()
    print(list2)


list_input = [5,7,8,9,"a", 'hello',"how",3,1]
print(list_input)
remove_string(list_input)