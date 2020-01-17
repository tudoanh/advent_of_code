import time
import itertools


class IntCode:
    def __init__(self, program=[]):
        self.program = program[:]
        self.index = 0
        self.relative_base = 0
        self.opcode = None
        self.first_mode = None
        self.second_mode = None
        self.first_param = None
        self.second_param = None
        self.value = None
        self.halted = False
        self.setted = False
        self.outputs = []
        self.inputs = []
        self.memory = {}

    def get_param(self):
        self.first_param = self.get_value_at(self.index + 1)
        if self.first_mode == 0:
            self.first_param = self.get_value_at(self.index + 1, position=True)
        if self.first_mode == 2:
            self.first_param = self.get_value_at(self.index + 1, relative=True)

        if self.opcode in [1, 2, 5, 6, 7, 8]:
            self.second_param = self.get_value_at(self.index + 2)
            if self.second_mode == 0:
                self.second_param = self.get_value_at(self.index + 2, position=True)
            if self.second_mode == 2:
                self.second_param = self.get_value_at(self.index + 2, relative=True)
        print(f"Index {self.index} - OPcode {self.opcode} - First mode {self.first_mode} - Second mode {self.second_mode} - First param {self.first_param} - Second param {self.second_param}")
        # time.sleep(0.5)

    def get_value_at(self, index, position=False, relative=False):
        if position:
            idx = self.program[index]
        elif relative:
            idx = self.program[index] + self.relative_base
        else:
            idx = index

        if idx < 0:
            raise IndexError

        if idx < len(self.program):
            return self.program[idx]
        else:
            # print(f"[Get] from memory instead - Index {idx} - Value {self.memory.get(idx, 0)}")
            return self.memory.get(idx, 0)

    def set_third_param(self, value):
        idx = self.index + 3
        if idx < len(self.program) and self.program[idx] < len(self.program):
            self.program[self.program[idx]] = value
        else:
            # print(f"Set to memory instead - Index {self.index + 3} - Value {value}")
            self.memory[self.program[idx]] = value

    def is_opcode(self, numb):
        n = str(numb).zfill(4)
        opcode = int(n[-2:])
        first_mode = int(n[1])
        second_mode = int(n[0])
        if first_mode not in [0, 1, 2] or second_mode not in [0, 1, 2]:
            return False
        if opcode in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.opcode = opcode
            self.first_mode = first_mode
            self.second_mode = second_mode
            return True

    def input(self, _input):
        self.program[self.first_param] = _input
        print(f"Write input {_input} to index {self.first_param}")
        self.index += 2

    def output(self):
        self.value = self.first_param
        self.outputs.append(self.value)
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

    def set_relative_base(self):
        self.relative_base += self.first_param
        self.index += 2

    def run(self, _input=None):
        while not self.halted:
            i = self.program[self.index]
            if i == 99:
                self.halted = True
                print("Halted")
                return self.outputs
            elif self.is_opcode(i):
                self.get_param()
                if self.opcode == 1:
                    self.add()
                elif self.opcode == 2:
                    self.multiply()
                elif self.opcode == 3:
                    self.input(_input)
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
                elif self.opcode == 9:
                    self.set_relative_base()
            else:
                self.index += 1
        return self.value


def test():
    ins = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    # ins = [104,1125899906842624,99]
    # ins = [1102,34915192,34915192,7,4,7,99,0]
    machine = IntCode(ins)
    print(machine.run())


if __name__ == '__main__':
    test()

    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        machine = IntCode(instruction)
        print(machine.run(1))

