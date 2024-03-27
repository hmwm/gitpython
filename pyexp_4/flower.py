def is_narcissistic(number):

    digits = str(number)
    n = len(digits)

    sum_of_digits = sum(int(digit) ** n for digit in digits)
    return sum_of_digits == number


for i in range(100, 1000):
    if is_narcissistic(i):
        print(i)

