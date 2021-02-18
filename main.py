import math as m
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
from scipy import spatial

plt.rcParams['figure.figsize'] = [5, 3]



filename = "SampleCoordinates.txt"

radius = 0.06


def read_coordinate_file(filename):
    """Läser .txt filer med lista över koordinater formaterade enligt {a, b} och listar dem som Mercator projection """
    def x_factor(b):
        x = b * m.pi/180
        return x

    def y_factor(a):
        y = np.log(m.tan((m.pi/4) + (a * m.pi/360)))
        return y

    x_lst = []
    y_lst = []

    with open(filename) as file:
        # Öppnar angivna filen
        for line in file:
            # Ta bort klutter och konvertera till Mercator projection
            line = line.strip("{}\n")
            a, b = line.split(',')
            x_lst.append(x_factor(float(b)))
            y_lst.append(y_factor(float(a)))
    coord_list = np.array([x_lst, y_lst])
    return coord_list


coord_list = read_coordinate_file(filename)
# print((read_coordinate_file(filename)))


def construct_graph_connections(coord_list, radius):
    """Funktion som svarar vilka koordinater som är inom givna radien till varandra samt avståndet mellan dem. """
    x = coord_list[0]  # koordinater
    y = coord_list[1]
    lst = []
    indices = []
    dist = []
    for nr, X in enumerate(x):  # numrerar listan
        lst.append([nr, X, y[nr]])

    for coord in lst:
        for coord_test in lst:
            r = m.sqrt(((coord_test[2]-coord[2])**2) + (coord_test[1]-coord[1])**2)  # Avståndsformeln
            if coord[0] == coord_test[0]:
                continue
            elif r < radius:
                indices.append([coord[0], coord_test[0]]) #med koordinater indices.append([coord[0], coord_test[0], [coord[1:3]], [coord_test[1:3]]])
                dist.append(r)

    return indices, dist


N = coord_list.shape[1]
distance = construct_graph_connections(coord_list, radius)[1]
indices = construct_graph_connections(coord_list, radius)[0]

def construct_graph(indices, distance, N):
    mtx = sp.csr_matrix((distance, np.array(indices).T), shape=(N, N))
    return mtx



def plot_points(coord_list):
    """Plottar och numrerar koordinater"""
    sz = coord_list.shape[1]
    n = np.linspace(1, sz, sz)
    fig, ax = plt.subplots(1, figsize=(10, 6))
    fig.suptitle('Koordinater')
    coord_x, coord_y = np.split(read_coordinate_file(filename), 2)
    plt.scatter(coord_x, coord_y)  # plottar givna koordinater
    coord_x = coord_x.reshape(sz, 1)
    coord_y = coord_y.reshape(sz, 1)
    for k, txt in enumerate(n):
        plt.annotate(txt-1, (coord_x[k], coord_y[k]))  # numrerar koordinaterna i plotten
    plt.show()


plot_points(read_coordinate_file(filename))

