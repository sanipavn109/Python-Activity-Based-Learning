a = int(input("Material cost: "))
b = int(input("Labour cost: "))
c = int(input("Selling price: "))

cost = a + b
profit = c - cost

print("Profit/Loss =", profit)

if profit > 0:
    print("Profit")
else:
    print("Loss")