time = "        51     69     98     78".split()
dist = "  377   1171   1224   1505".split()
product = 1
for i in range(4):
    total = 0
    for j in range(int(time[i])):
        if j * (int(time[i]) - j) > int(dist[i]):
            total += 1
    product *= total

print(product)