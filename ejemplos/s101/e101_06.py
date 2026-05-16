import pandas
from matplotlib import pyplot

ventas = pandas.read_csv("../../conjuntos/ventas.csv", encoding="latin-1")

print(ventas)

ventas_conteos = ventas.groupby("fecha").size()

print(ventas_conteos)

diferencias = ventas_conteos.diff(1)

figure, axis = pyplot.subplots(2, 1, height_ratios=(1, 2))

diferencias.plot.bar(ax=axis[0])
ventas_conteos.plot(ax=axis[1])

pyplot.show()