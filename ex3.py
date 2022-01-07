tuples_x = [1, 2, 3, 4, 5]
tuples_y = [6, 7, 8, 9, 10]
result = 0
for n1, n2 in zip(tuples_x, tuples_y):
    result = result + (n1*n2)
print(result)

count = 0
for x in range(100):
    if x % 2 == 0:
        count += 1
print(count)

oddPairs = 0
pairs = ((4, 5), (6, 7), (8, 9))
for x, y in pairs:
    if x % 2 != 0 and y % 2 != 0:
        oddPairs += 1
print(oddPairs)