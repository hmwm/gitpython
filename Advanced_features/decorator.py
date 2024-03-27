# 使用装饰器 减少代码复用
# 保证被装饰函数自身逻辑清晰（一个原则）
# 可以通过装饰器扩展包装别人的代码，而不是到第三方库里修改源码
import time


def decorator(func):
    # wrapper会实现原本函数的功能并且扩充新功能
    def wrapper(*args, **kwargs):
        # 扩充功能
        stat_time = time.time()
        # 原本函数功能
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {end_time - stat_time} second.")
        return result

    return wrapper


@decorator
def sqrt(x):
    return x * x


# 装饰
decorator_sqrt = decorator(sqrt)
print(decorator_sqrt(10))

sqrt = decorator(sqrt)
print(sqrt(10))

# @decorator帽子装饰函数
print(sqrt(10))




