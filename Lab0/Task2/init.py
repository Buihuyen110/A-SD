n = 0
a1 = open('D:\\Python\\CTDL&GT\\Lab0\\Task2\\input.txt', 'r')
n = int(a1.readline())
f0, f1 = 0, 1
for _ in range (2, n+1):
    f0, f1 = f1, f0+f1
a2 = open('D:\\Python\\CTDL&GT\\Lab0\\Task2\\output.txt', 'w')
a2.write(str(f1))