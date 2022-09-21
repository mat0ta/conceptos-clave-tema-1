from punto import Punto
from rectangulo import Rectangulo
from totareadme import readme

if __name__ == "__main__":
    readme('C:/Users/marti/Documents/GitHub/conceptos-clave-tema-1')
    print("\nActividad del punto:\n\n")
    p = Punto()
    print(p)
    print(p.cuadrante())
    print(p.vector())
    print(p.distancia())
    print("\nActividad del rectángulo:\n\n")
    r = Rectangulo()
    print(r.base())
    print(r.altura())
    print(r.area())