a = 42
b = 20
if a > b:
    a = b
else:
    b -= 10

print(" a ", a)

none = True

flag = 10

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

strList = ["hello", "world", "zhangsan", "lisi"]

for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + " X " + str(i) + " = " + str(i * j) + "\t", end=" ")
    print("")

a = "*"

for i in range(1, 10):
    for j in range(1, i + 1):
        print(a + "\t", end="")
    print("")
