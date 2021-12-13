def no_teen_sum(a,b,c):
    x=[a,b,c]
    s=0
    for i in x:
        if 13<=i<=19:
            s+=fix_teen(i)
        else:
            s+=i
    return s

def fix_teen(n):
    if n!=15 and n!=16:
        return 0
    else:
        return n
print(no_teen_sum(1,2,3))
print(no_teen_sum(2,13,1))
print(no_teen_sum(2,1,14))
print(no_teen_sum(2,13,15))
print(no_teen_sum(2,16,15))


