<h1 align="center">CONCEPTOS-CLAVE-TEMA-1</h1>

En este [repositorio](https://github.com/mat0ta/conceptos-clave-tema-1) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: [mat0ta](https://github.com/mat0ta).

<h2>Ejercicio de los puntos</h2>

Se debe crear una clase llamada Punto con constructor para crear las coordenadas de los puntos de con las funciones: cuadrante, vector y distancia.

El código empleado para crear dicho algoritmo es el siguiente:

```py

class Punto():
    def __init__(self):
        self.puntos = []
        self.x = 0
        self.y = 0
        while True:
            try:
                self.n_puntos = int(input('Introduce el número de puntos que quieres crear: '))
                for i in range(self.n_puntos):
                    punto = input('Introduce las coordenadas del punto {} separados por una coma: '.format(i + 1))
                    self.puntos.append(punto.split(','))
                break
            except ValueError:
                print('Introduce un número porfavor.')
    def __str__(self):
        for i in range(self.n_puntos):
            self.x = int(self.puntos[i][0])
            self.y = int(self.puntos[i][1])
            print("El punto {} se encuentra en el {}".format(i + 1, self.cuadrante()))
        while True:
            try:
                numero = int(input('Introduce el número del punto que quieres utilizar para el resto del ejericio: '))
                self.x = int(self.puntos[numero - 1][0])
                self.y = int(self.puntos[numero - 1][1])
                break
            except ValueError:
                print('Introduce un número porfavor.')
        return("El punto seleccionado es: ({},{})".format(self.x, self.y))

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
                for i in range(self.n_puntos):
                    print("{}: ({}, {})".format(i + 1, self.puntos[i][0], self.puntos[i][1]))
                decision = int(input('Introduce el numero del punto que quieres usar como segundo punto (Vector): '))
                x_2 = int(self.puntos[decision - 1][0])
                y_2 = int(self.puntos[decision - 1][1])
                break
            except ValueError:
                print('Introduce un número porfavor.')
        return("({},{})".format(x_2 - self.x, y_2 - self.y))

    def distancia(self):
        while True:
            try:
                for i in range(self.n_puntos):
                    print("{}: ({}, {})".format(i + 1, self.puntos[i][0], self.puntos[i][1]))
                decision = int(input('Introduce el numero del punto que quieres usar como segundo punto (Distancia): '))
                x_2 = int(self.puntos[decision - 1][0])
                y_2 = int(self.puntos[decision - 1][1])
                break
            except ValueError:
                print('Introduce un número porfavor.')
        return((x_2 - self.x)**2 + (y_2 - self.y)**2)**0.5

```

<h2>Ejercicio del rectángulo</h2>

Crea una clase llamada Rectángulo con constructor y las funciones: base, altura y area.

El código empleado para crear dicho algoritmo es el siguiente:

```py

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
```

