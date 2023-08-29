# Find the anagrams in the string and print 
# race = acer cat=tac hat=tah
input = " race cat tac acer hat tah yes care"

l = input.split()
d ={}

for word in l:
    sorted_word = "".join(sorted(word))
    if(sorted_word in d):
        d[sorted_word].append(word)
    else:
        d[sorted_word] =[word]
for key in d:
    if len(d.get(key)) >1:
        list = d.get(key)
        for i in range(len(list)):
            if i==len(list)-1:
                print(list[i], end="")
            else:
                print(list[i] + "=", end="")
        print()
