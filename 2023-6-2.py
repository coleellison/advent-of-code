time = 51699878
dist = 377117112241505

i = 1
while (i * (time - i)) < dist:
    i += 1

total = time - (2 * i) + 1
print(total)