# 1 пример - raise
def greet_person(person_name):
    if person_name == 'ВоланДеМорт':
        raise Exception('Мы не произносим его имени...')
    print(f'Привет! {person_name}')


print(greet_person('Студент'))
print(greet_person('ВоланДеМорт'))

# Traceback (most recent call last):
#   File "C:\Users\belae\PycharmProjects\HW_Urban_Modul_8\CocnpectCreateExceptions.py", line 9, in <module>
#     print(greet_person('ВоланДеМорт'))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\belae\PycharmProjects\HW_Urban_Modul_8\CocnpectCreateExceptions.py", line 4, in greet_person
#     raise Exception('Мы не произносим его имени...')
# Exception: Мы не произносим его имени...
# 2 пример - обработка ошибки raise перед
try:
    raise NameError('Приветики!')
except NameError as exc:
    print(f'Исключение типа {type(exc)} прошло мимо! Его параметры: {exc.args}')
    raise
class ProZero(Exception):
    pass


def f(a, b):
    if b == 0:
        raise ProZero('Деление на 0 невозможно!')
    return a / b


print(f(5, 0))
#-----------------------------------------------
class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero('Деление на 0 невозможно!', {'a': a, 'b': b})
    return a / b


try:
    result = f(10, 0)
except ProZero as e:
    print(f'Error!\n Message about error: {e.message}\n Extra information: {e.extra_info}')