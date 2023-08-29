#HCF - Highest common factor or gretest common divison (GCD)
# of two numbers is the lasrgest positive integer that perfectly divides
# the two given number

def hcf_or_gcd(x,y):
    first = set()
    second = set()
    for i in range(2,x+1):
        if x%i == 0:
            first.add(i)
    for i in range(2,y+1):
        if y%i == 0:
            second.add(i)
    x = first.intersection(second) 
    print(max(x))

hcf_or_gcd(150, 200)

def second_hcf_or_gcd(x,y):
    small =min(x,y)
    for i in range(1,small+1):
        if x%i == 0 and y%i==0:
            hcf = i
    print(hcf)
hcf_or_gcd(6, 60)