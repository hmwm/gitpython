dic_1 = {'Tom': 21, 'Bob': 18, 'Jack': 23, 'Ana': 20}
dic_2 = {'李华': 21, '韩梅梅': 18, '小明': 23, '小红': 20}

n = int(input("请输入需要排序的个数："))
if n > len(dic_1):
    n = len(dic_1)

print(sorted(dic_1.keys())[:n])
print(sorted(dic_2.values())[:n])

