a = int(input("Basic salary: "))
b = int(input("Allowance: "))
c = int(input("Bonus: "))

total = a + b + c
net = total - total * 10 / 100

print("Gross Salary =", total)
print("Net Salary =", net)