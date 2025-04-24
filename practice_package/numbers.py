calculate_distance = lambda x, y: abs(x - y)

calculate_segments = lambda a, b: int(a / b)


calculate_digit_sum = lambda num: sum(int(digit) for digit in str(abs(num)))

def round_to_multiple(num, mul):
    return mul * round(num / mul)

def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)
