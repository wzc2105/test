# # def fun_1(b):
# #     if b!=0:
# #         lst = [2,8]
# #         for i in range(1,b):
# #             lst.append(lst[-1]+lst[-2])
# #             return lst[-2]%lst[-1]
# # print(fun_1(66))
# import random
# k=int(input("enter:"))
# lst=[random.randint(1,100) for i in range(k)]#列表生成
# def getmax(lst):
#     x=lst[0]
#     for i in range(1,len(lst)):#遍历1-lst长度
#         if lst[i]>x:
#             x=lst[i]
#     return x
# print(lst,getmax(lst))
import torch
print(torch.__version__)
