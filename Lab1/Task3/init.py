n = 0
with open('input.txt', 'r') as file:
    n = file.read()
    n = int(n)
    f0, f1 = 0, 1
    for _ in range(2, n+1):
        f0, f1 = f1, (f0 + f1) % 10
with open('output.txt', 'w') as file:
    file.write(str(f1 % 10))
