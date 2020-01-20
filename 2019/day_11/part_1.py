from intcode import IntCode


class Painting:
    def __init__(self, input_vals, initial_color=0):
        self.computer = IntCode(input_vals)
        self.direction = 0
        self.x, self.y = 0, 0
        self.painted = {(self.x, self.y): initial_color}

    def paint(self):
        while not self.computer.halted:
            starting_color = self.painted[(self.x, self.y)] if (self.x, self.y) in self.painted else 0
            color = self.computer.run(starting_color)
            self.painted[(self.x, self.y)] = color
            self.change_direction(self.computer.run(color))
            self.rotate()

    def change_direction(self, rotate_direction):
        if rotate_direction == 0:
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

    def rotate(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        p = Painting(instruction)
        p.paint()
        print(len(p.painted.keys()))
