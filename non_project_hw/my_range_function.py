def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        raise ValueError("Step cannot be zero")
    if not (isinstance(start, (int, float)) and isinstance(stop, (int, float)) and isinstance(step, (int, float))):
        raise TypeError("Start, stop and step must be a numbers")
    if stop > start and step < 0:
        raise ValueError("wrong data")
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    if step < 0:
        while current > stop:
            yield current
            current += step


