check_between_numbers = lambda A, B, C: (B > A and B < C) \
      or (B < A and B > C)  

check_odd_three = lambda num: 99 < abs(num) < 1000 \
    and abs(num) % 2  

check_unique_digits = lambda num: 99 < abs(num) < 1000 \
    and len(set(str(num))) >= 3  


def check_palindrome_number(number):
    num_str = str(abs(int(number)))
    return num_str == num_str[::-1]


def check_ascending_digits(number):
    pass
