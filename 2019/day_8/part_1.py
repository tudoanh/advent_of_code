import numpy as np
import collections


def fill_layer(pixels, width, height):
    layer = np.zeros((height, width))
    i = 0
    for x in range(height):
        for y in range(width):
            layer[x][y] = pixels[i]
            i += 1
    return layer.astype(int)

def data_to_layers(data, width, height):
    numb_of_layers = len(data) // (width * height)
    jump = len(data) // numb_of_layers
    layers = []
    i = 0
    for x in range(numb_of_layers):
        layers.append(fill_layer(data[i:i+jump], width, height))
        i += jump
    return layers


def find_password(_input, img_width, img_height):
    layers = data_to_layers(_input, img_width, img_height)
    counters = [collections.Counter(layer.flatten()) for layer in layers]
    return sorted(counters, key=lambda x: x[0])


def test():
    f = find_password('123456789012', 3, 2)
    print(f)


if __name__ == '__main__':
    # test()
    with open('./input.txt', 'rt') as f:
        _input = f.readline().strip()
        counters = find_password(_input, 25, 6)
        print(counters[0][1] * counters[0][2])
