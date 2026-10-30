a = [100, 200, 300, 100, 400, 200]

for i in a:
    if a.count(i) > 1:
        print("Duplicate:", i)
        a.remove(i)