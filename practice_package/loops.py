def sum_even_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            total += digit
        number = number // 10

    return total


def count_vowel_triplets(text):
    vowels = "aeiouy"
    text = text.lower()
    count = 0
    for i in range(len(text) - 2):
        if text[i] in vowels and text[i + 1] in vowels \
            and text[i + 2] in vowels:
            count += 1
    return count


def find_fibonacci_index(number):
    if number < 1:
        return -1

    a, b = 1, 1
    index = 1

    while a <= number:
        if a == number:
            return index
        a, b = b, a + b
        index += 1

    return -1


def remove_duplicates(string):
    if not string:
        return string

    result = string[0]

    for char in string[1:]:
        if char != result[-1]:
            result += char

    return result