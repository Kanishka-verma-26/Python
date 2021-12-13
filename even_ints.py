def count_even(a):
    c=0
    for i in range(len(a)):
        if a[i]%2==0:
            c+=1
    return c
print(count_even([2,1,2,3,4]))
print(count_even([2,2,0]))
print(count_even([1,3,5]))
