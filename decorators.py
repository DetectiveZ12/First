def my_dec(my_func):
    def upper_my_func(*args, **kwargs):
        result = my_func(*args, **kwargs)
        return result.upper()
    return upper_my_func

@my_dec
def my_func(name):
    return name

print(my_func("atharv"))