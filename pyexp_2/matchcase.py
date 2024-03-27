score = int(input("请输入你的成绩(1-100)："))
level_create_map = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "E"
}
# 字典无序，需要手动排序(高到低)

for key in sorted(level_create_map.keys(), reverse=True):
    if score > key:
        result = level_create_map[key]
        print(result)
        break


