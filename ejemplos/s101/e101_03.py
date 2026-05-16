import numpy

ventas = numpy.array([13, 15, 17, 19, 32, 23, 22, 18, 21, 16, 12, 11])

print(ventas)

diferencias = numpy.diff(ventas, 1)

print(diferencias)