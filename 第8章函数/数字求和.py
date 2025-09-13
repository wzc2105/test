import random
import re
k=input("enter:")
def get_sum(k):
    findall=re.findall(r'\d+',str(k))
    sum=0
    for i in findall:
        sum+=int(i)
    return sum
print(get_sum(k))