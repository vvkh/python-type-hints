def add(something, other):
    # какие методы есть у something?
    return something + other


# ide пытается
result = add(5, 5)
print(result)

result = add('5', '5')
print(result)

# не всегда правильно
result = add(5, '5')
print(result)
