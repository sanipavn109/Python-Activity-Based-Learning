u = int(input("Enter units: "))

if u <= 100:
    b = u * 2
elif u <= 200:
    b = 200 + (u - 100) * 3
else:
    b = 500 + (u - 200) * 5

print("Bill =", b)