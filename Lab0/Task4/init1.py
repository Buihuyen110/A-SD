import time
n = 0
with open("input.txt", "r") as file:
    n = file.read()
    n = int(n)
f0, f1 = 0, 1
t_start = time.perf_counter()
for _ in range (2, n+1):
    f0, f1 = f1, f0+f1
t_stop = time.perf_counter()
print("Elapsed time during the whole program in seconds:", t_stop-t_start)
with open('output.txt', "w") as file:
    file.write(str(f1))



    
    
