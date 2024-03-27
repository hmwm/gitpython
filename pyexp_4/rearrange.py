def rearrange_array(arr):
    even = [i for i in arr if i % 2 == 0]
    odd = [i for i in arr if i % 2 == 1]
    return even + odd


array_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = rearrange_array(array_test)
print(result)
