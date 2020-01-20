from intcode import IntCode
import turtle


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def draw(instruction):
    machine = IntCode(instruction)
    output = machine.run(output=False)
    parsed = chunks(output, 3)

    scale = 20

    tiles = {}

    for x, y, _id in parsed:
        if _id == 2:
            tiles[(x, y)] = True

    print(len(tiles.keys()))


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        draw(instruction)
