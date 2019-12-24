def main():
    with open('./input.txt', 'rt') as f:
        input = f.readlines()
        input = [i.strip() for i in input]
    modules_mass = [int(m) for m in input]

    total_fuel = 0

    for mass in modules_mass:
        total_fuel += (int(mass / 3) - 2)

    return total_fuel


if __name__ == '__main__':
    print(main())  #3262358
