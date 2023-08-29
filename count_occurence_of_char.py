def count_occurence_of_a_char(str, char):
    l = sorted(str)
    count =l.count(char)
    print(count)
count_occurence_of_a_char("hello how are you?","l")
def count_occurence_of_a_char_other_way(str, char):
    count =0
    for i in range(len(str)):
        if char == str[i]:
            count += 1
    print(count)
count_occurence_of_a_char_other_way("hello how are you?","l")
print("hello how are you?".count("l"))