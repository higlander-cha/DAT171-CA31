import numpy as np
import math

filename = "SampleCoordinates.txt"


def read_coordinare_file(filename):
    # Funktioner för att räkna om värderna {a,b} till Mercator projection
    def x_factor(b):
        x = b * math.pi/180
        return x

    def y_factor(a):
        y = np.log(math.tan((math.pi/4) + (a * math.pi/360)))
        return y

    x_lst = list()
    y_lst = list()

    with open(filename) as file:
        # Öppnar angivna filen
        for line in file:
            # Ta bort klutter och konvertera till Mercator projection
            line = line[1:7]
            a, b = line.split(',') # HÄR är separeringen jag behövde för att få scriptet att fungera.
            a = float(a)
            b = float(b)
            a = y_factor(a)
            b = x_factor(b)
            x_lst.append(a)
            y_lst.append(b)

    coord = np.array([x_lst, y_lst])
    # print(coord)
    # print(x_lst)
    # print(type(x_lst))
    # print(y_lst)

    return coord


print((read_coordinare_file(filename)))