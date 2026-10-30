a = int(input("Venue cost: "))
b = int(input("Food cost: "))
c = int(input("Transport cost: "))

total = a + b + c

s = int(input("Sponsorship: "))
n = int(input("Participants: "))

if n > 0:
    fee = (total - s) / n
    print("Participant Fee =", fee)
else:
    print("Invalid participants")