def end_other(a,b):
    x=a.lower()
    y=b.lower()
    if len(x)>len(y):
        if y == x[len(x)-len(y):]:
            return True
    elif len(y)>len(x):
        if x==y[len(y)-len(x):]:
            return True
    return False
print(end_other("Hiabc","abc"))
print(end_other("AbC","HiaBc"))
print(end_other("abc","abXabc"))


