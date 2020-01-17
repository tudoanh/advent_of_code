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
        self.third_mode = None
        self.first_param = None
        self.second_param = None
        self.third_param = None
        self.value = None
        self.halted = False
        self.setted = False
        self.outputs = []
        self.inputs = []
        self.memory = {}
        self.valid_opcodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.writable = [1, 2, 5, 6, 7, 8]
        self.length = len(program)

    def get_param(self):
        position = True if self.first_mode == 0 else False
        relative = True if self.first_mode == 2 else False
        write = True if self.opcode == 3 else False
        self.first_param = self.get_value_at(self.index + 1, position, relative, write)

        if self.opcode in [1, 2, 5, 6, 7, 8]:
            position = True if self.second_mode == 0 else False
            relative = True if self.second_mode == 2 else False
            self.second_param = self.get_value_at(self.index + 2, position, relative)

            position = True if self.third_mode == 0 else False
            relative = True if self.third_mode == 2 else False
            self.third_param = self.get_value_at(self.index + 3, position, relative, write=True)

        print(f"{self.index} | OPCode {self.opcode} | 1st M {self.first_mode} | 1st V {self.first_param} | 2nd M {self.second_mode} | 2nd V {self.second_param} | 3rd M {self.third_mode} | 3rd {self.third_param}")

    def get_value_at(self, index, position=False, relative=False, write=False):
        if position:
            idx = self.program[index]
        elif relative:
            idx = self.program[index] + self.relative_base
        else:
            idx = index

        if idx < 0:
            raise IndexError

        if write:
            return idx

        if idx < self.length:
            return self.program[idx]
        else:
            return self.memory.get(idx, 0)

    def set_third_param(self, value):
        if self.third_param < self.length:
            self.program[self.third_param] = value
        else:
            self.memory[self.third_param] = value

    def is_opcode(self, numb):
        n = str(numb).zfill(5)
        opcode = int(n[-2:])
        first_mode = int(n[2])
        second_mode = int(n[1])
        third_mode = int(n[0])
        if first_mode not in [0, 1, 2] or second_mode not in [0, 1, 2] or third_mode not in [0, 2]:
            return False
        if opcode in self.valid_opcodes:
            self.opcode = opcode
            self.first_mode = first_mode
            self.second_mode = second_mode
            if opcode in self.writable:
                self.third_mode = third_mode
            return True

    def input(self, _input):
        if self.first_param < self.length:
            self.program[self.first_param] = _input
        else:
            self.memory[self.first_param] = _input

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
    # test()

    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        machine = IntCode(instruction)
        print(machine.run(1))

