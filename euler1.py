def metodo_euler(f, x0, y0, xf, h):

    x = x0
    y = y0
    while x < xf:
        pend = f(x, y)
        y += h * pend
        x += h
    return y

def main():
    
    def f(x, y):
        return 0.2 * x * y  


    x0 = float(input("Ingrese el valor inicial de x: "))
    y0 = float(input("Ingrese el valor inicial de y(x0): "))
    xf = float(input("Ingrese el valor final de x para el que desea aproximar y: "))
    h = float(input("Ingrese el tamaño del paso: "))

    
    aproximacion = metodo_euler(f, x0, y0, xf, h)
    print("Aproximación de y en x={}: {}".format(xf, aproximacion))

if __name__ == "__main__":
    main()
