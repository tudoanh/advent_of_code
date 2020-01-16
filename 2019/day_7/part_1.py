class IntCode():
    def __init__(self, program=[], _input=0, setting=0):
        self._input = _input
        self.setting = setting
        self.program = program
        self.index = 0
        self._output = []
        self.opcode = None
        self.first_mode = None
        self.second_mode = None
        self.first_param = None
        self.second_param = None
        self.input_count = 0
        self.value = 0

    def get_param(self):
        try:
            self.first_param = self.program[self.index + 1]
            if self.first_mode == 0:
                self.first_param = self.get_value_at(self.index + 1)

            if self.opcode in [1, 2, 5, 6, 7, 8]:
                self.second_param = self.program[self.index + 2]
                if self.second_mode == 0:
                    self.second_param = self.get_value_at(self.index + 2)
            print(f"OPcode {self.opcode} - First mode {self.first_mode} - Second mode {self.second_mode} - First param {self.first_param} - Second param {self.second_param}")
        except IndexError:
            pass

    def is_opcode(self, numb):
        n = str(numb).zfill(4)
        opcode = int(n[-2:])
        first_mode = int(n[1])
        second_mode = int(n[0])
        if first_mode not in [0, 1] or second_mode not in [0, 1]:
            return False
        if opcode in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.opcode = opcode
            self.first_mode = first_mode
            self.second_mode = second_mode
            return True

    def set_third_param(self, value):
        try:
            self.program[self.program[self.index + 3]] = value
        except IndexError as e:
            pass

    def input(self):
        if self.input_count == 0:
            self.program[self.program[self.index + 1]] = self.setting
            self.index += 2
        if self.input_count == 1:
            self.program[self.program[self.index + 1]] = self._input
            self.index += 2
        self.input_count += 1

    def output(self):
        self.value = self.first_param
        self.index += 2

    def add(self):
        self.set_third_param(self.first_param + self.second_param)
        self.index += 4

    def multiply(self):
        self.set_third_param(self.first_param * self.second_param)
        self.index += 4

    def jump_if_true(self):
        if self.first_param != 0:
            self.index = self.second_param
        else:
            self.index += 2

    def jump_if_false(self):
        if self.first_param == 0:
            self.index = self.second_param
        else:
            self.index += 2

    def less_than(self):
        if self.first_param < self.second_param:
            self.set_third_param(1)
        else:
            self.set_third_param(0)
        self.index += 4

    def equal(self):
        if self.first_param == self.second_param:
            self.set_third_param(1)
        else:
            self.set_third_param(0)
        self.index += 4

    def get_value_at(self, index):
        return self.program[self.program[index]]

    def run(self):
        self.index = 0
        while self.index < len(self.program):
            if self.index == len(self.program):
                break
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
                elif self.opcode == 5:
                    self.jump_if_true()
                elif self.opcode == 6:
                    self.jump_if_false()
                elif self.opcode == 7:
                    self.less_than()
                elif self.opcode == 8:
                    self.equal()
            elif i == 99:
                break
            else:
                self.index += 1
        return self.value


def test():
    settings = [4, 3, 2, 1, 0]
    output = 0
    instruction = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    for s in settings:
        output = IntCode(instruction, setting=s, _input=output).run()
    assert output == 43210


if __name__ == '__main__':
    # test()
    import itertools
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        result = 0
        for phases in itertools.permutations(range(5)):
            output = 0
            for s in phases:
                output = IntCode(instruction, setting=s, _input=output).run()
            if result < output:
                result = output
        print(result)

