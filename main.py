from punto import Punto
from rectangulo import Rectangulo
from totareadme import readme

if __name__ == "__main__":
    readme('C:/Users/marti/Documents/GitHub/conceptos-clave-tema-1')
    print("\nActividad del punto:\n\n")
    p = Punto()
    print(p)
    print("El punto se encuentra en el {}".format(p.cuadrante()))
    print("El vector creado entre los puntos es: {}".format(p.vector()))
    print("La distancia entre los puntos es de: {}".format(p.distancia()))
    print("\nActividad del rectángulo:\n\n")
    r = Rectangulo()
    print(r.base())
    print(r.altura())
    print(r.area())