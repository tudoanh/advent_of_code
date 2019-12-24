def test():
    assert best_total_steps(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']) == 30
    assert best_total_steps(
        ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    ) == 610
    assert best_total_steps(
        ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    ) == 410


def draw(path):
    drew_path = []
    X, Y = (0, 0)
    for trace in path:
        direction = trace[0]
        steps = int(trace[1:])
        if direction == 'R':
            drew_path += [(X + n, Y) for n in range(1, steps + 1)]
            X += steps
        if direction == 'U':
            drew_path += [(X, Y + n) for n in range(1, steps + 1)]
            Y += steps
        if direction == 'L':
            drew_path += [(X - n, Y) for n in range(1, steps + 1)]
            X -= steps
        if direction == 'D':
            drew_path += [(X, Y - n) for n in range(1, steps + 1)]
            Y -= steps
    return drew_path


def best_total_steps(first_path, second_path):
    first_wire_map = draw(first_path)
    second_wire_map = draw(second_path)

    intersection_points = list(set(first_wire_map).intersection(second_wire_map))
    def steps(point):
        # We will add 2 more steps because index start from 0, but steps count from 1
        return first_wire_map.index(point) + second_wire_map.index(point) + 2

    return min([steps(p) for p in intersection_points])


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readlines()
        input = [i.strip() for i in input]
        first_wire_path = input[0].split(',')
        second_wire_path = input[1].split(',')
        print(best_total_steps(first_wire_path, second_wire_path))
