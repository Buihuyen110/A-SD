n = 0
a1 = open('D:\\Python\\CTDL&GT\\Lab0\\Task3\\input.txt', 'r')
a2 = open('D:\\Python\\CTDL&GT\\Lab0\\Task3\\output.txt', 'w')
n = int(a1.read())
f0, f1 = 0, 1
for _ in range(2, n+1):
    f0, f1 = f1, (f0 + f1) % 10
a2.write(str(f1 % 10))
