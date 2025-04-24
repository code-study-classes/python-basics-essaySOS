def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    discount = amount * 0.1 if amount >= 5000 else amount * 0.05 if \
        amount >= 1000 else 0
    return round(discount, 2)


def describe_number(n):
    even = 'четное' if n % 2 == 0 else 'нечетное'
    digits = ('одиночное' if len(str(n)) == 1
          else 'двузначное' if len(str(n)) == 2
          else 'трехзначное')
    return f"{even} {digits} число"


def convert_to_meters(unitNumber, lengthInUnits):
    match unitNumber:
        case 1:
            return lengthInUnits * 0.1
        case 2:
            return lengthInUnits * 1000
        case 3:
            return lengthInUnits * 1
        case 4:
            return lengthInUnits * 0.001
        case 5:
            return lengthInUnits * 0.01
        case _:
            return lengthInUnits


def describe_age(age):
    pass