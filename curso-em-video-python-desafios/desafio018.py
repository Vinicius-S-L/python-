from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do angulo: '))
print("o valor em coseno é {:.2f}, seno é {:.2f} e a tangente é {}".format(cos(radians(angulo)), sin(radians(angulo)), tan(radians(angulo))))

