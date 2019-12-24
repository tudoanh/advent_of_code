def get_fuel(x):
    return int(x / 3) - 2


def total_fuel(mass):
    total = 0
    while get_fuel(mass) >= 0:
        mass = get_fuel(mass)
        total += mass
    return total


def main():
    with open('./input.txt', 'rt') as f:
        input = f.readlines()
        input = [i.strip() for i in input]
    modules_mass = [int(m) for m in input]

    fuel_requirements = sum([total_fuel(mass) for mass in modules_mass])
    return fuel_requirements


if __name__ == '__main__':
    print(main())  #4890696
