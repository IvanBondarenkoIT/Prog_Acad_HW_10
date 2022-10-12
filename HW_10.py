# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок 0,5,10,15,20,25
#  та відповіддю програми має бути число 30.
LIMIT_OF_POWERS = 10
step = 0


def is_arithmetic(args):
    global step
    list_ = []
    for idx, item in enumerate(args[::-1]):
        list_.append(args[-idx] - item)
    list_ = list_[1::]
    step = list_[0]
    return all(x == list_[0] for x in list_)


def is_geometric(args):
    global step
    list_ = []
    for idx, item in enumerate(args[::-1]):
        list_.append(args[-idx] / (1 if item == 0 else item))
    list_ = list_[1::]
    step = list_[0]
    return all(x == list_[0] for x in list_)


def is_power(args):
    global step
    for i in range(2, LIMIT_OF_POWERS):
        list_ = []
        for idx, item in enumerate(args):
            list_.append(round(item ** (1 / i)) / (idx + 1))
        step = (len(args) + 1) ** i
        if all(x == list_[0] for x in list_):
            return True


def sequences(*args):
    if is_arithmetic(args):
        return f"for {args} - Answer {int(args[-1] + step)}"
    elif is_geometric(args):
        return f"for {args} - Answer {int(args[-1] * step)}"
    elif is_power(args):
        return f"for {args} - Answer {step}"
    else:
        return "Sorry i don't know the answer"


print(sequences(0, 2, 4, 6, 8, 10, 12))  # 14
print(sequences(1, 4, 7, 10, 13))  # 16
print(sequences(1, 2, 4, 8, 16, 32))  # 64
print(sequences(1, 3, 9, 27))  # 81
print(sequences(1, 4, 9, 16, 25))  # 36
print(sequences(1, 8, 27, 64, 125))  # 216
print(sequences(0, 5, 10, 15, 20, 25))  # 30
# print(input())

# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром,
#  одержаний множенням двох трицифрових чисел. Виведіть значення цього паліндрому і те,
#  множенням яких чисел він є."""


def is_palindrome(num):
    str_num = str(num)
    if len(str_num) % 2:
        return False
    return str_num == str_num[::-1]


def find_max_palindrome(x, y):
    while not is_palindrome(x * y):
        if x > 0:
            x -= 1
        else:
            y -= 1
            x = 999
    return f"Result {x} * {y} = {x*y}"


print(find_max_palindrome(99, 99))
print(find_max_palindrome(999, 999))
