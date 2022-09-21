class Punto():
    def __init__(self):
        while True:
            try:
                x = int(input('Introduce la coordenada X: '))
                self.x = x
                y = int(input('Introduce la coordenada Y: '))
                self.y = y
                break
            except ValueError:
                print('Introduce un número porfavor.')
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x > 0:
            if self.y > 0:
                return "1er Cuadrante"
            elif self.y < 0:
                return "4to Cuadrante"
            else:
                return "Eje X"
        elif self.x < 0:
            if self.y > 0:
                return "2do Cuadrante"
            elif self.y < 0:
                return "3er Cuadrante"
            else:
                return "Eje X"
        elif self.x == 0:
            return "Eje Y"

    def vector(self):
        while True:
            try:
                x = int(input('Introduce la coordenada X del segundo punto (Vector): '))
                x_2 = x
                y = int(input('Introduce la coordenada Y del primer punto (Vector): '))
                y_2 = y
                break
            except ValueError:
                print('Introduce un número porfavor.')
        return("({},{})".format(x_2 - self.x, y_2 - self.y))

    def distancia(self):
        while True:
            try:
                x = int(input('Introduce la coordenada X del segundo punto (Distancia): '))
                x_2 = x
                y = int(input('Introduce la coordenada Y del primer punto (Distancia): '))
                y_2 = y
                break
            except ValueError:
                print('Introduce un número porfavor.')
        return((x_2 - self.x)**2 + (y_2 - self.y)**2)**0.5