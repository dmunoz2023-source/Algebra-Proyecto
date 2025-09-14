import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

def graficar_funcion(expr, punto=None, dominio=None, recorrido=None):
    """
    Grafica la función expr en un rango razonable.
    Si se pasa punto (x0, y0), lo resalta en la gráfica.
    """

    x_min, x_max = -10, 10  # por defecto

    xs, ys = []
    pasos = 400
    delta = (x_max - x_min) / pasos

    for i in range(pasos + 1):
        val = x_min + i * delta
        try:
            y_val = expr.subs(x, val).evalf()
            if y_val.is_real:
                xs.append(float(val))
                ys.append(float(y_val))
        except Exception:
            pass

    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, label='f(x)', color='blue')

    # Resaltar punto evaluado
    if punto is not None:
        try:
            if punto[1] is not None:
                plt.scatter([punto[0]], [punto[1]], color='red',
                            label=f'Punto evaluado ({punto[0]}, {punto[1]:.3f})', zorder=5)
        except Exception:
            pass

    # Sombrear recorrido si es intervalo
    try:
        if recorrido is not None and isinstance(recorrido, sp.Interval):
            yi, yf = float(recorrido.start.evalf()), float(recorrido.end.evalf())
            plt.axhspan(yi, yf, color='orange', alpha=0.1, label='Recorrido')
    except Exception:
        pass

    plt.title('Gráfica de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
