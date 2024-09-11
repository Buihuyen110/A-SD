with open("input.txt", "r") as file:
    a,b = map(int, input().split())
with open("output.txt", "w") as file:
    file.write(str(a+b))