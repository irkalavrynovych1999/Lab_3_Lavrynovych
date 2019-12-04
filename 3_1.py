def super_suma(*args):
    nums = args
    suma = 0

    print('Обчислюємо: ', *args)

    for n in nums:
        if type(n) == int or type(n) == float:
            suma += n
        else:
            print('{} не число, його порпускаємо'.format(n))

    return suma


s0 = super_suma(1)
print('Сума = ', s0)
print('*'*15)

s1 = super_suma(2, 4.4, 'Hello')
print('Сума = ', s1)
print('*'*15)

s2 = super_suma(1, 2, 3, 4, 10, 15, 10.4)
print('Сума = ', s2)
print('*'*15)