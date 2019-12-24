import re


def test():
    assert meet_rule(111111) == True
    assert meet_rule(223456) == True
    assert meet_rule(223450) == False
    assert meet_rule(123789) == False


def never_decrease(n):
    list_number = [int(i) for i in list(str(n))]
    if sorted(list_number) != list_number:
        return False
    return True


def adjacent_is_same(n):
    if re.search(r'(\d)\1', str(n)):
        return True


def meet_rule(n):
    if never_decrease(n) and adjacent_is_same(n):
        return True
    return False


if __name__ == '__main__':
    count = 0
    for n in range(271973, 785962):
        if meet_rule(n):
            count += 1
    print(count)

