def test():
    assert intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def intcode(instruction, opcode_index=0):
    sequence = instruction[opcode_index:opcode_index+4]
    if sequence[0] == 1:
        instruction[sequence[3]] = instruction[sequence[1]] + instruction[sequence[2]]
    if sequence[0] == 2:
        instruction[sequence[3]] = instruction[sequence[1]] * instruction[sequence[2]]
    if instruction[opcode_index + 4] == 99:
        return instruction
    else:
        return intcode(instruction, opcode_index=opcode_index + 4)


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        # To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
        instruction[1] = 12
        instruction[2] = 2
        print(intcode(instruction)[0])

