fruits = (('apple', 2.5), ('banana', 1.7), ('orange', 3.6), ('grape', 5.2))
fruit_name = input("请输入水果名称：")

found = False
for fruit, price in fruits:
    if fruit_name.lower() == fruit:
        print(f"{fruit_name}的价格是{price}")
        found = True
        break

if not found:
    print("未找到该水果！")

# 使用字典的查找效率O(1)
fruit_hash = {
    'apple': 1.7,
    'banana': 3.6,
    'orange': 5,
    'grape': 6
}
fruit_name = input("请输入水果名：").lower()

if fruit_name in fruit_hash:
    print(f"{fruit_name}的价格时{fruit_hash[fruit_name]}")
else:
    print("未找到")
