def divade(a, b):
    try:
        result = a / b
        print('Result calculated')
        return result
    except ZeroDivisionError as ex:
        print(f'an error occured: {ex}')

divade(456565, 3454)
divade(4, 0)