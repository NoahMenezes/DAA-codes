
from fractions import Fraction
def knapsack(weight, profit, capacity):
    n = len(weight)
    print("\n1. Fractional Strategy")
    print("2. Least Weight Strategy")
    print("3. Maximum Profit Strategy")
    print("4. Ratio Strategy")
    choice = int(input("Enter Choice: "))
    x = [0] * n
    remain = capacity
    if choice == 1:

        for i in range(n):
            x[i] = Fraction(1, i + 2)
    elif choice == 2:
        order = sorted(range(n), key=lambda i: weight[i])
        for i in order:

            if remain >= weight[i]:
                x[i] = 1
                remain -= weight[i]

            else:
                x[i] = Fraction(remain, weight[i])
                break
    elif choice == 3:
        order = sorted(range(n), key=lambda i: profit[i], reverse=True)
        for i in order:
            if remain >= weight[i]:
                x[i] = 1
                remain -= weight[i]
            else:
                x[i] = Fraction(remain, weight[i])
                break
    elif choice == 4:
        order = sorted(
            range(n),
            key=lambda i: profit[i] / weight[i],
            reverse=True
        )
        for i in order:
            if remain >= weight[i]:
                x[i] = 1
                remain -= weight[i]
            else:
                x[i] = Fraction(remain, weight[i])
                break
    else:
        print("Invalid Choice")
        return
    total_w = 0
    total_p = 0
    for i in range(n):
        total_w += weight[i] * float(x[i])
        total_p += profit[i] * float(x[i])
    print("\nSelected Fractions:", x)
    print("Net Weight =", total_w)
    print("Net Profit =", total_p)
n = int(input("Enter No. of Elements: "))
capacity = int(input("Enter Knapsack Capacity: "))
print("\nEnter Weights:")
weight = []
for i in range(n):
    weight.append(int(input()))
print("\nEnter Profits:")
profit = []
for i in range(n):
    profit.append(int(input()))
ratio = []
for i in range(n):
    ratio.append(profit[i] / weight[i])
print("\nProfit/Weight Ratio:", ratio)
print("\nUsing Greedy Algorithm:")
knapsack(weight, profit, capacity)
