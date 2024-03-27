def count_char(str_input):
    letter_count = 0
    digit_count = 0
    other_count = 0

    for char in str_input:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    print("字母数量为：", letter_count)
    print("数字数量为：", digit_count)
    print("其他字符数量为：", other_count)


str_input = input("请输入一个字符串：")
count_char(str_input)