def vowel_or_consonant(char):
    l = ['a','e','i','o','u']

    if char.lower() in l:
        print("It's a vowel")
    else:
        print("It's a consonant")

vowel_or_consonant('w')

def vowel_or_consonant_method2(char):
    l = "aeiouAEIOU"
    if l.find(char) != -1:
        print("It's a vowel")
    else:
        print("It's a consonant")
vowel_or_consonant_method2('w')