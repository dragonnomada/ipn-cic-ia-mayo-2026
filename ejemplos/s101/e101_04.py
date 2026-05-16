import numpy
from matplotlib import pyplot

ventas = numpy.array([13, 15, 17, 19, 32, 23, 22, 18, 21, 16, 12, 11])

diferencias = numpy.diff(ventas, 1)

pyplot.plot(ventas)
pyplot.bar(numpy.arange(diferencias.size) + 1, diferencias)

pyplot.show()