str_name = input("请输入一组人名：")
some_name_list = str_name.split(',')
dedup_name_list = []
for i in some_name_list:
    if i not in dedup_name_list:
        dedup_name_list.append(i)
print(dedup_name_list)
#Sally,Bob,Michael,Bob,Sally,Smith

str_name = input("请输入一组人名：")
some_name_list = str_name.split(',')
dedup_name_list = []
[dedup_name_list.append(name.strip()) for name in some_name_list if name.strip() not in dedup_name_list]
print(dedup_name_list)

