import tkinter as tk 
from tkinter import messagebox, scrolledtext
from funciones import parsear_funcion, calcular_dominio, calcular_intersecciones, calcular_recorrido, evaluar_funcion
from graficos import graficar_funcion
from utils import validar_valor_x
import sympy as sp
import math

x = sp.symbols('x')

class AnalizadorFuncionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Funciones MatemÃ¡ticas")

        # Entrada funciÃ³n
        tk.Label(root, text="Ingrese la funciÃ³n f(x):").grid(row=0, column=0, sticky='w')
        self.funcion_entry = tk.Entry(root, width=50)
        self.funcion_entry.grid(row=0, column=1, padx=5, pady=5)

        # Entrada valor opcional
        tk.Label(root, text="Ingrese valor de x (opcional):").grid(row=1, column=0, sticky='w')
        self.valor_x_entry = tk.Entry(root, width=20)
        self.valor_x_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        # Botones
        self.analizar_btn = tk.Button(root, text="Analizar", command=self.analizar_funcion)
        self.analizar_btn.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Resultados:").grid(row=3, column=0, sticky='nw')
        self.resultados_text = scrolledtext.ScrolledText(root, width=70, height=20)
        self.resultados_text.grid(row=3, column=1, padx=5, pady=5)

        self.graficar_btn = tk.Button(root, text="Graficar funciÃ³n", command=self.graficar)
        self.graficar_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # Variables
        self.expr = None
        self.punto_evaluado = None
        self.dominio = None
        self.recorrido = None

    def analizar_funcion(self):
        """Analiza la funciÃ³n ingresada y muestra resultados"""
        self.resultados_text.delete('1.0', tk.END)
        funcion_str = self.funcion_entry.get().strip()
        valor_x_str = self.valor_x_entry.get().strip()

        if not funcion_str:
            messagebox.showerror("Error", "Debe ingresar una funciÃ³n.")
            return

        # Parsear
        try:
            self.expr = parsear_funcion(funcion_str)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Dominio y recorrido
        self.dominio = calcular_dominio(self.expr)
        self.resultados_text.insert(tk.END, f"Dominio de la funciÃ³n:\n{self.dominio}\n\n")

        self.recorrido = calcular_recorrido(self.expr, self.dominio)
        self.resultados_text.insert(tk.END, f"Recorrido (rango) de la funciÃ³n:\n{self.recorrido}\n\n")

        # Intersecciones
        intersecciones_x, interseccion_y = calcular_intersecciones(self.expr)
        self.resultados_text.insert(tk.END, "Intersecciones con el eje x (raÃ­ces):\n")
        if intersecciones_x:
            for raiz in intersecciones_x:
                self.resultados_text.insert(tk.END, f"x = {raiz}\n")
        else:
            self.resultados_text.insert(tk.END, "No se encontraron intersecciones con el eje x.\n")

        self.resultados_text.insert(tk.END, f"\nIntersecciÃ³n con el eje y (x=0):\n")
        self.resultados_text.insert(tk.END, f"f(0) = {interseccion_y}\n\n")

        # EvaluaciÃ³n en x opcional
        if valor_x_str:
            try:
                valor_x = validar_valor_x(valor_x_str)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return

            try:
                resultado, paso_a_paso = evaluar_funcion(self.expr, valor_x)

                if resultado is None or math.isnan(float(resultado)) or math.isinf(float(resultado)):
                    messagebox.showerror("Error", f"x = {valor_x} no pertenece al dominio de la funciÃ³n.")
                    self.punto_evaluado = None
                else:
                    self.resultados_text.insert(tk.END, f"EvaluaciÃ³n en x = {valor_x}\n")
                    self.resultados_text.insert(tk.END, paso_a_paso + "\n")
                    self.resultados_text.insert(tk.END, f"Punto evaluado: ({valor_x}, {resultado})\n")
                    self.punto_evaluado = (valor_x, float(resultado))

            except Exception as e:
                messagebox.showerror("Error", f"Error al evaluar la funciÃ³n: {e}")
                self.punto_evaluado = None
        else:
            self.punto_evaluado = None

    def graficar(self):
        """Muestra la grÃ¡fica de la funciÃ³n"""
        if self.expr is None:
            messagebox.showerror("Error", "Primero debe analizar una funciÃ³n vÃ¡lida.")
            return
        try:
            graficar_funcion(self.expr, punto=self.punto_evaluado, dominio=self.dominio, recorrido=self.recorrido)
        except Exception as e:
            messagebox.showerror("Error", f"Error al graficar: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorFuncionesApp(root)
    root.mainloop()
