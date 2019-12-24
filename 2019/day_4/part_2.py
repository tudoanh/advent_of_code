import re

def test():
    assert adjacent_is_same(677777) == False
    assert adjacent_is_same(456666) == False
    assert adjacent_is_same(112233) == True
    assert adjacent_is_same(123444) == False
    assert adjacent_is_same(111122) == True
    assert adjacent_is_same(111233) == True


def never_decrease(n):
    list_number = [int(i) for i in list(str(n))]
    if sorted(list_number) != list_number:
        return False
    return True


def adjacent_is_same(n):
    n = str(n)
    search = re.findall(r'(\d)\1|(\d)\1\1', n)
    if search:
        di = {repeated[0]: n.count(repeated[0]) for repeated in search}
        check = []
        for k, v in di.items():
            check.append(v)
        checked = [v == 2 for v in check]
        if any(checked):
            return True
        return False


def meet_rule(n):
    if never_decrease(n) and adjacent_is_same(n):
        return True
    return False


if __name__ == '__main__':
    test()
    count = 0
    for n in range(271973, 785962):
        if meet_rule(n):
            print(n)
            count += 1
    print(count)


