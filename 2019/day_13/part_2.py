from intcode import IntCode
import turtle


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def draw(instruction):
    machine = IntCode(instruction)
    _id = None

    scale = 20

    turtle.speed(0)
    turtle.ht()
    turtle.tracer(0)

    marker = turtle.Turtle()

    marker.penup()

    score = 0

    tiles = {}

    while not machine.halted:
        x = machine.run(_id)
        y = machine.run(x)
        _id = machine.run(y)

        if x == -1 and y == 0:
            score = _id
        else:
            marker.goto(x=x * scale, y=y * scale)
            if _id == 0:
                obj = ''
            elif _id == 1:
                obj = '|'
            elif _id == 2:
                obj = '='
                tiles[(x, y)] = obj
            elif _id == 3:
                obj = '_'
            elif _id == 4:
                obj = 'O'
            marker.write(obj)

        marker.goto(-100, 300)
        marker.write(f"Score: {score}")

    turtle.mainloop()



if __name__ == '__main__':
    with open('./input.txt', 'rt') as f:
        input = f.readline().strip()
        instruction = [int(i) for i in input.split(',')]
        draw(instruction)
