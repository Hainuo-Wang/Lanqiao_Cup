import time

def Cal_Ti(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time: %lf secs.' % (func.__name__, t2 - t1))
        return result

    return wrapper