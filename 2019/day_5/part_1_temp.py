def test():
    assert intcode([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]


def intcode(instruction, opcode_index=0, input=None):
    if instruction[opcode_index] == 3:
        input_index = instruction[opcode_index + 1]
        instruction[input_index] = input
        return intcode(instruction, opcode_index=opcode_index + 2, input=input)
    if instruction[opcode_index] == 4:
        pointer = 2
        output_index = instruction[opcode_index + 1]
        instruction[output_index] = output_index
        return intcode(instruction, opcode_index=opcode_index + 2, input=input)

    pointer = 4
    sequence = instruction[opcode_index:opcode_index + pointer]
    print(sequence)

    opcode = str(sequence[0])
    param_1, param_2, param_3 = sequence[1:]
    mode_1 = mode_2 = mode_3 = 0

    if len(opcode) == 4:
        opcode = '0' + opcode
        mode_3, mode_2, mode_1 = opcode[:3]
        opcode = opcode[-2:]

    if mode_1 == '0':
        param_1 = instruction[param_1]

    if mode_2 == '0':
        param_2 = instruction[param_2]


    if opcode in ['1', '01']:
        instruction[param_3] = param_1 + param_2
    elif opcode in ['2', '02']:
        instruction[param_3] = param_1 * param_2

    if instruction[opcode_index + pointer] == 99:
        return instruction
    else:
        return intcode(instruction, opcode_index=opcode_index + pointer, input=input)


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        print(intcode(instruction))
