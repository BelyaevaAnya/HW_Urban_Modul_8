# 2 типа ошибок
# 1) Синтаксическая
# test = 'aaa
# print(test)
#     test = 'aaa
#            ^
# SyntaxError: unterminated string literal (detected at line 3)
# 2) Исключения
# test = 0
# print(10 / test)
#     print(10 / test)
#           ~~~^~~~~~
# ZeroDivisionError: division by zero
# https://docs.python.org/3/library/exceptions.html