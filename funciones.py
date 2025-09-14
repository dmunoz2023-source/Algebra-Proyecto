import sympy as sp

# Definimos el símbolo independiente x para las funciones
x = sp.symbols('x')

def parsear_funcion(funcion_str):
    """
    Parsea la función ingresada como string a una expresión sympy.
    Lanza ValueError si la función es inválida o mal escrita.
    """
    try:
        expr = sp.sympify(funcion_str)
        return expr
    except (sp.SympifyError, TypeError) as e:
        raise ValueError("Función inválida o mal escrita.") from e

def calcular_dominio(expr):
    """
    Calcula el dominio de la función usando continuous_domain de Sympy.
    Retorna un conjunto de Sympy representando el dominio en los Reales.
    """
    try:
        from sympy.calculus.util import continuous_domain
        dominio = continuous_domain(expr, x, sp.S.Reals)
        return dominio
    except Exception:
        return sp.S.Reals

def calcular_intersecciones(expr):
    """
    Calcula las intersecciones con los ejes x y y.
    - Intersección con eje x: soluciones reales de f(x) = 0.
    - Intersección con eje y: valor de f(0).
    Retorna dos valores: lista de raíces y valor en x=0.
    """
    soluciones = sp.solve(expr, x)
    intersecciones_x = [s for s in soluciones if s.is_real]

    try:
        interseccion_y = expr.subs(x, 0)
    except Exception:
        interseccion_y = None

    return intersecciones_x, interseccion_y

def calcular_recorrido(expr, dominio_condicion):
    """
    Calcula el recorrido (rango) de la función en el dominio dado.
    Usa sympy.calculus.util.function_range si es posible.
    Si no, intenta aproximar evaluando en un intervalo.
    """
    try:
        from sympy.calculus.util import function_range
        rango = function_range(expr, x, dominio_condicion)
        return rango
    except Exception:
        # Aproximación simple: evaluar en puntos del dominio
        try:
            xs = [i for i in range(-10, 11)]
            ys = []
            for val in xs:
                try:
                    y_val = expr.subs(x, val).evalf()
                    if y_val.is_real:
                        ys.append(float(y_val))
                except Exception:
                    continue
            if ys:
                return sp.Interval(min(ys), max(ys))
        except Exception:
            pass
        return "No se pudo determinar el recorrido."

def evaluar_funcion(expr, valor_x):
    """
    Evalúa la función en el valor_x dado.
    Retorna el resultado numérico y un texto con paso a paso:
    - Sustitución de x.
    - Evaluación numérica.
    """
    paso_a_paso = f"Sustituyendo x = {valor_x} en la función:\n"
    expr_sustit = expr.subs(x, valor_x)
    paso_a_paso += f"f({valor_x}) = {expr_sustit}\n"

    try:
        resultado = expr_sustit.evalf()
        paso_a_paso += f"Evaluando numéricamente: {resultado}"
    except Exception as e:
        resultado = None
        paso_a_paso += f"Error al evaluar numéricamente: {e}"

    return resultado, paso_a_paso
