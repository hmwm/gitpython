while True:
    n = int(input("请输入0到100之间的正整数:"))
    if 0 < n <= 100:
        break
    else:
        print("输入数不合法，请重新输入：")


factor = [i for i in range(2, n) if n % i == 0]
sum_of_factor = sum(factor)

print(factor, sum_of_factor)


