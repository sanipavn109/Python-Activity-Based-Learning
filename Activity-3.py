a = int(input("Consultation: "))
b = int(input("Test: "))
c = int(input("Treatment: "))

total = a + b + c

if total >= 5000:
    total = total - total * 10 / 100

print("Final Bill =", total)