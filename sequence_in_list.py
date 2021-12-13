def arrayCheck(li):
    a=[1,2,3]
    for i in a:
        if i in li:
            continue
        else:
            return False
    return True
print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))
