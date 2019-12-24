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
        # The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.
        for noun in range(100):
            for verb in range(100):
                new_instrunction = instruction[:]
                new_instrunction[1] = noun
                new_instrunction[2] = verb
                if intcode(new_instrunction)[0] == 19690720:
                    print(noun)
                    print(verb)
                    break
        # noun, verb = (25, 5)

