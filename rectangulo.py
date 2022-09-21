class Rectangulo():
    def __init__(self):
        while True:
            try:
                x = input('Introduce las coordenadas del punto inicial separados por una coma: ')
                self.inicial = x.split(',')
                y = input('Introduce las coordenadas del punto final separados por una coma: ')
                self.final = y.split(',')
                break
            except ValueError:
                print('Introduce unas coordenadas correctas porfavor.')
    def base(self):
        return("La base del rectangulo tiene como coordenadas iniciales: ({}, {}) y como coordenadas finales: ({}, {})".format(self.inicial[0], self.inicial[1], self.final[0], self.inicial[1]))
    def altura(self):
        return("La altura del rectangulo tiene como coordenadas iniciales: ({}, {}) y como coordenadas finales: ({}, {})".format(self.inicial[0], self.inicial[1], self.inicial[0], self.final[1]))
    def area(self):
        return("El area del rectangulo es de {} unidades".format(abs((int(self.final[0]) - int(self.inicial[0])) * (int(self.final[1]) - int(self.inicial[1])))))

if __name__ == "__main__":
    r = Rectangulo()
    print(r.base())
    print(r.altura())
    print(r.area())