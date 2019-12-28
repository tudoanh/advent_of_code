class IntCode():
    def __init__(self, program=[], _input=1):
        self._input = _input
        self.program = program
        self.index = 0
        self._output = []
        self.opcode = None
        self.first_mode = None
        self.second_mode = None
        self.first_param = None
        self.second_param = None
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
        self.program[self.program[self.index + 1]] = self._input
        self.index += 2

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
    assert IntCode([3,9,8,9,10,9,4,9,99,-1,8], 8).run() == 1  # Check if input == 8, 1 is True, 0 is false
    assert IntCode([3,9,8,9,10,9,4,9,99,-1,8], 5).run() == 0
    assert IntCode([3,9,7,9,10,9,4,9,99,-1,8], 8).run() == 0  # X < 8?
    assert IntCode([3,9,7,9,10,9,4,9,99,-1,8], 3).run() == 1
    assert IntCode([3,3,1108,-1,8,3,4,3,99], 8).run() == 1    # X == 8?
    assert IntCode([3,3,1108,-1,8,3,4,3,99], 5).run() == 0
    assert IntCode([3,3,1107,-1,8,3,4,3,99], 20).run() == 0   # X < 8?
    assert IntCode([3,3,1107,-1,8,3,4,3,99], 6).run() == 1    # X < 8?
    assert IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0).run() == 0
    assert IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], -4).run() == 1
    assert IntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0).run() == 0
    assert IntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 5).run() == 1

    check_8 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    assert IntCode(check_8, 6).run() == 999
    assert IntCode(check_8, 8).run() == 1000
    assert IntCode(check_8, 12).run() == 1001


if __name__ == '__main__':
    # test()
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        intcode = IntCode(program=instruction, _input=5)
        print(f"Answer: {intcode.run()}")
