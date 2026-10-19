from MergeSort import merge_sort
from fractions import Fraction
import time 
import random
def knapsack(weight, profit, capacity):
    choice=int(input("Enter choice: "))
    n=len(weight)
    x=[0]*n
    remain=capacity

    if choice==1:
        for i in range(n):
            x[i]=Fraction(1,i+2)
    elif choice==2:
        order=sorted(range(n), key=lambda i:weight[i])
        for i in order:
            if remain>=weight[i]:
                x[i]=1
                remain-=weight[i]
            else:
                x[i]=Fraction(remain, weight[i])
                break
    elif choice==3:
        order=sorted(range(n), key=lambda i:weight[i], reverse=True)

        for i in order:
            if remain>=weight[i]:
                x[i]=1
                remain-=weight[i]
            else:
                x[i]=Fraction(remain, weight[i])
                break
    elif choice==4:
        order=sorted(range(n), key=lambda i:profit[i]/weight[i], reverse=True)

        for i in order:
            if remain>=weight[i]:
                x[i]=1
                remain-=weight[i]
            else:
                x[i]=Fraction(remain, weight[i])
                break
    else:
        print("invalid")
        return 
    total_w=0
    total_p=0
    for i in range(n):
        total_w+=weight[i]*float(x[i])
        total_p+=weight[i]*float(x[i])
    print(x)
    print(total_w)
    print(total_p)
n=int(input("Enter the inputs: "))
capacity=int(input("Enter the capacity: "))
print("Enter the weights: ")
weight=[]
for i in range(n):
    weight.append(int(input()))
print("Enter the profit: ")
profit=[]
for i in range(n):
    profit.append(int(input()))
ratio=[]
print("Enter the ratio: ")
for i in range(n):
    ratio.append(profit[i]/weight[i])
print(ratio)
knapsack(weight, profit, capacity)


