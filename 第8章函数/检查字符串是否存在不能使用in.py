lst=input("enter str:")
i=input("enter i:")
import re
def esist(lst,s):
    lst1=list(lst)
    find1=re.findall(s,str(lst1))
    if find1:
        return True
    else:
        return False
    print(esist(lst,i))
print(esist(lst,i))
