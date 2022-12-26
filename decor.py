import time

def spent_time(func):
    """ Декорирующая функция
        Считает время затрачиваемое функцией на выполнение
        the "hello" function spent 8 seconds
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        total = int(round(((end - start) * 1000), 0))
        print()
        if total < 1000:
            print(f'the "{func.__name__}" function spent: {total} ms')
        elif (total//1000) < 60:
            print(f'the "{func.__name__}" function spent: {total//1000:02d}:{total%1000:03d} sec')
        elif ((total//1000)//60) < 60:
            print(f'the "{func.__name__}" function spent: {(total//1000)//60:02d}:{(total//1000)%60:02d} min')
        else:
            print(f'the "{func.__name__}" function spent: {((total//1000)//60)//60}:{((total//1000)//60)%60:02d} h')
        print('-' * 40)
    return wrapper

def return_delta_time(start: float, name: str):
    end = time.time()
    total = int(round(((end - start) * 1000), 0))
    print()
    if total < 1000:
        print(f'the "{name}" function spent: {total} ms')
    elif (total//1000) < 60:
        print(f'the "{name}" function spent: {total//1000:02d}:{total%1000:03d} sec')
    elif ((total//1000)//60) < 60:
        print(f'the "{name}" function spent: {(total//1000)//60:02d}:{(total//1000)%60:02d} min')
    else:
        print(f'the "{name}" function spent: {((total//1000)//60)//60}:{((total//1000)//60)%60:02d} h')
    print('-' * 20)