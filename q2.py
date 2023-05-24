binary__num = input("Enter the binary number : ")

decimal__num = 0
p = 0

for i in range(len(binary__num)):
    x=int(binary__num[i])
    decimal__num = decimal__num + x * (2**(len(binary__num) - i - 1))

print(decimal__num)