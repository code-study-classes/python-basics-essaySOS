extract_file_name = lambda full_file_name: (  # noqa: E731
    full_file_name.split('/')[-1] if 
        full_file_name.split('/')[-1].startswith('.')
    else full_file_name.split('/')[-1].split('.')[0]
)


def encrypt_sentence(sentence):
    start = sentence[::2]
    end = sentence[1::2]
    return end + start[::-1]


def check_brackets(expression):
    otkr = 0
    zakr = 0
    pos = 0
    for i in range(0, len(expression)):
        if expression[i] != ' ':
            pos += 1
        if expression[i] == '(':
            otkr += 1
        elif expression[i] == ')':
            zakr += 1
        if zakr > otkr:
            return pos
    if otkr > zakr:
        return -1
    return 0


def reverse_domain(domain):
    prt = domain.split('.')
    if len(prt) == 1:
        return domain
    return '.'.join(reversed(prt))


def count_vowel_groups(word):
    pass