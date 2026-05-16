import numpy

ventas = numpy.array([13, 15, 17, 19, 32, 23, 22, 18, 21, 16, 12, 11])

print(ventas)

ventas_desplazadas = numpy.roll(ventas, 1)

print(ventas_desplazadas)

ventas1 = ventas[1:]
ventas2 = ventas_desplazadas[1:]

print(ventas1)
print(ventas2)

diferencias = ventas1 - ventas2

print(diferencias)