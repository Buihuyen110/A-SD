import time
n = 0
a1 = open('D:\\Python\\CTDL&GT\\Lab0\\Task4\\input.txt', 'r')
a2 = open('D:\\Python\\CTDL&GT\\Lab0\\Task4\\output.txt', 'w')
n = int(a1.read())
f0, f1 = 0, 1
t_start = time.perf_counter()
for _ in range (2, n+1):
    f0, f1 = f1, f0+f1
t_stop = time.perf_counter()
print('время работы', t_stop-t_start)
a2.write(str(f1))



    
    
