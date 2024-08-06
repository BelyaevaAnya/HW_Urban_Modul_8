def calc(line, mode = 0):
    """
    :param line:
    :param mode: mode = 0-print all operations; mode = 1-print only errors
    :return:
    """
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if mode == 0:
        if operation == '+':
            print(f'Result: {operand_1+operand_2}')
        if operation == '-':
            print(f'Result: {operand_1 - operand_2}')
        if operation == '/':
            print(f'Result: {operand_1 / operand_2}')
        if operation == '//':
            print(f'Result: {operand_1 // operand_2}')
        if operation == '%':
            print(f'Result: {operand_1 % operand_2}')
        if operation == '*':
            print(f'Result: {operand_1 * operand_2}')



cnt = 0
with open('calc.txt', 'r') as file_obj:
    for line in file_obj:
        try:
            # calc(line, 0)
            calc(line, 1)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Error in line: {cnt}\nNo data for operation\nError: {exc}\nParametrs: {exc.args}')
            else:
                print(f'Error in line: {cnt}\nNo way to convert number\nError: {exc}\nParametrs: {exc.args}')