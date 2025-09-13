i=input("enter:")

def lower_uper(s):
    lst=[]
    for i in s:
        if i.islower():
            lst.append(i.upper())
        elif i.isupper():
            lst.append(i.lower())
        else:
            lst.append(i)
    return ''.join(lst)
print(lower_uper(i))