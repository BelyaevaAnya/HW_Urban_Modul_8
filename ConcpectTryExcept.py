# try:
#     # пишем код с возможной ошибкой
# except:
#     # пишем здесь блок кода в случае возникновения ошибки
# try:
#     i = 0
#     print(10/i)
#     print('Done')
# except ZeroDivisionError as exe:
#     print(f'Zero division is error! Error: {exe}')
# # => Zero division is error!

try:
    file = open('blablabla.txt')
except OSError as exc:
    print(f'{exc}-вот ошибка, {exc.args}-вот параметры, но мы работаем')
# => [Errno 2] No such file or directory: 'blablabla.txt'-вот ошибка,
# (2, 'No such file or directory')-вот параметры, но мы работаем
i = int(input('Enter number: '))
try:
    result = 10*(1/i)
except ZeroDivisionError as exc:
    print(f'No zero division! {exc}')
else:
    print('We didnt make wrong division')
finally:
    print('Thats all')