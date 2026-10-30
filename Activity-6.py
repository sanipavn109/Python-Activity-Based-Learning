p = int(input("Enter price: "))
q = int(input("Enter quantity: "))

total = p * q

if total >= 1000:
    total = total - total * 10 / 100

print("Final Bill =", total)