ventas = [13, 15, 17, 19, 32, 23, 22, 18, 21, 16, 12, 11]

print(ventas)

ventas_desplazadas = ventas[:]

ventas_desplazadas.insert(0, 0)
ventas_desplazadas.pop()

print(ventas_desplazadas)

ventas1 = ventas[1:]
ventas2 = ventas_desplazadas[1:]

print(ventas1)
print(ventas2)

diferencias = [v1 - v2 for v1, v2 in zip(ventas1, ventas2)]

print(diferencias)