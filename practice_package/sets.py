def find_common_elements(set1, set2):
    return set1.intersection(set2)


def is_superset(set_a, set_b):
    return set_b.issubset(set_a)


def remove_duplicates(items):
    return list(dict.fromkeys(items))


def count_unique_words(text):
    return len(set(text.lower().split()))


def find_shared_items(*sets):
    return set.intersection(*sets)
