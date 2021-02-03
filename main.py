import numpy as np
import math

filename = "SampleCoordinates.txt"

#Måste vara integers för att funktionerna ska fungera
def x_factor(b):
    x = b * math.pi/180
    return x


def y_factor(a):
    y = np.log(math.tan((math.pi/4) + (a * math.pi/360)))
    return y

# def read_coordinare_file(filename):


lst = ''


with open(filename) as file:
    print(type(file))

# tar bort klutter
    for line in file:
        line = line.replace('}', '')
        line = line.replace('{', '')
        line = line.replace(' ', '')
        lst = lst + line
#får ut en sträng som ser bra ut
print(type(lst))
print(lst)

#Delar upp strängen i en lista med coordinaterna.
lst_split = lst.split('\n')
print(type(lst_split))
print(lst_split)





