class IntCode():
    def __init__(self, program=[], _input=1):
        self._input = _input
        self.program = program
        self.valid_ops = [1, 2, 3, 4, 101, 102, 1001, 1002, 1101, 1102]
        self.index = 0
        self._output = []
        self.opcode = None
        self.first_mode = None
        self.second_mode = None
        self.first_param = None
        self.second_param = None

    def get_param(self):
        self.first_param = self.program[self.index + 1]
        if self.first_mode == 0:
            self.first_param = self.get_value_at(self.index + 1)

        if self.opcode in [1, 2]:
            self.second_param = self.program[self.index + 2]
            if self.second_mode == 0:
                self.second_param = self.get_value_at(self.index + 2)
        print(f"OPcode {self.opcode} - First mode {self.first_mode} - Second mode {self.second_mode} - First param {self.first_param} - Second param {self.second_param}")

    def is_opcode(self, numb):
        n = str(numb).zfill(4)
        opcode = int(n[-2:])
        if opcode in [1, 2, 3, 4]:
            self.opcode = opcode
            self.first_mode = int(n[1])
            self.second_mode = int(n[0])
            return True

    def input(self):
        self.program[self.program[self.index + 1]] = self._input
        self.index += 2

    def output(self):
        value = self.first_param
        if value != 0:  # This will be the answer
            print(f'Value {value}')
            raise ValueError('Program failed')
        self._output.append(value)
        self.index += 2

    def add(self):
        self.program[self.program[self.index + 3]] = self.first_param + self.second_param
        self.index += 4

    def multiply(self):
        self.program[self.program[self.index + 3]] = self.first_param * self.second_param
        self.index += 4

    def get_value_at(self, index):
        return self.program[self.program[index]]

    def run(self):
        self.index = 0
        while True:
            i = self.program[self.index]
            if self.is_opcode(i):
                self.get_param()
                if self.opcode == 1:
                    self.add()
                elif self.opcode == 2:
                    self.multiply()
                elif self.opcode == 3:
                    self.input()
                elif self.opcode == 4:
                    self.output()
                elif i == 99:
                    break
            else:
                self.index += 1


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        intcode = IntCode(program=instruction, _input=1)
        intcode.run()
