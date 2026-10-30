s = input("Enter feedback: ").lower()

score = 0

if "good" in s or "nice" in s:
    score = score + 1

if "bad" in s or "poor" in s:
    score = score - 1

print("Score =", score)