d = int(input("Enter distance: "))
age = int(input("Enter age: "))

fare = d * 2

if age >= 60:
    fare = fare / 2

print("Fare =", fare)