import pandas
from matplotlib import pyplot

ventas = pandas.Series([13, 15, 17, 19, 32, 23, 22, 18, 21, 16, 12, 11])

diferencias = ventas.diff(1)

figure, axis = pyplot.subplots(2, 1, height_ratios=(1, 2))

diferencias.plot.bar(ax=axis[0])
ventas.plot(ax=axis[1])

pyplot.show()