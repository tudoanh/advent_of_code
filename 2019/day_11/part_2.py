from intcode import IntCode
import turtle
import time


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def paint(instruction):
    machine = IntCode(instruction)

    turtle.speed(0)
    turtle.ht()
    turtle.tracer(0)

    marker = turtle.Turtle()

    marker.penup()
    marker.left(90)

    dot_distance = 10

    painted = {}

    color = 1
    direction = 1

    while not machine.halted:
        color = machine.run(direction)
        direction = machine.run(color)

        marker.write('#' if color == 1 else '.')

        if direction == 1:
            marker.right(90)
        elif direction == 0:
            marker.left(90)

        marker.forward(dot_distance)

    turtle.mainloop()


if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        paint(instruction)
