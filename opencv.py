f = open("E:\实验文件夹\pytest.txt", "r", encoding="utf-8")
print(f.read())
f.close()

#等价于下面
with open("E:\实验文件夹\pytest.txt", "r", encoding="utf-8") as f_2:
    print(f_2.read())
