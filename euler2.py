def metodo_euler(f, I0, t0, tf, h):

    t = t0
    I = I0
    while t < tf:
        pend = f(t, I)
        I += h * pend
        t += h
    return I

def circuit_current(t, I):

    return 15 - 3 * I


I0 = 0
t0 = 0
tf = 0.5  
h = 0.01  


aproximacion = metodo_euler(circuit_current, I0, t0, tf, h)
print("Corriente en el circuito medio segundo después de cerrar el interruptor:", aproximacion, "A")
