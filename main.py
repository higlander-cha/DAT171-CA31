import numpy as np
import math
# %config InlineBackend.figure_formats = ['svg']
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [5, 3]

filename = "SampleCoordinates.txt"


def read_coordinate_file(filename):
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
            a, b = line.split(',')  # HÄR är separeringen jag behövde för att få scriptet att fungera.
            x_lst.append(x_factor(float(b)))
            y_lst.append(y_factor(float(a)))

    coord_list = np.array([x_lst, y_lst])
    # print(coord)
    # print(x_lst)
    # print(type(x_lst))
    # print(y_lst)

    return coord_list

coord_list = read_coordinate_file(filename)
# print((read_coordinate_file(filename)))

def plot_points(coord_list):
    sz = coord_list.shape[1]
    n = np.linspace(1, sz, sz)
    fig, ax = plt.subplots(1, figsize=(10, 6))
    fig.suptitle('Koordinater')
    coord_x, coord_y = np.split(read_coordinate_file(filename), 2)
    plt.scatter(coord_x, coord_y)
    coord_x = coord_x.reshape(sz, 1)
    coord_y = coord_y.reshape(sz, 1)
    for k, txt in enumerate(n):
        plt.annotate(txt-1, (coord_x[k], coord_y[k]))
    plt.show()


# plot_points(read_coordinate_file(filename))

# def construct_graph_connections(coord_list, radius):


lst = []
radius = 0.1
print(coord_list)


coord_list = coord_list.reshape((coord_list.shape[1], 2))

for X, element1 in enumerate(coord_list):
    print(element1[1])

    for Y, element2 in enumerate(coord_list):

        r = (((element2[0] - element1[0]) ** 2) + element2[1] - element1[1] ** 2) ** 0.5
        if abs(r) < radius:
            lst.append([X, element1, Y, element2, r])
        else:
            continue
print(lst)

#Här blir det fel med
# for nr, element in enumerate(coord_list):
#     x = element[0]
#     y = ele
#     # r = (((element2[0]-element1[0])**2) + element2[1]-element1[1]**2) ** 0.5
#     # if abs(r) < radius:
#     #     lst.append([X, element1, Y, element2, r])
#     # else:
#     #     continue
# print(lst)

