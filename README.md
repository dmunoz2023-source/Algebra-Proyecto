# Algebra-Proyecto

Analizador de Funciones Matemáticas
Este proyecto es una aplicación en Python con interfaz gráfica (Tkinter) que permite analizar funciones matemáticas de manera simbólica y gráfica.

Los usuarios pueden:
- Ingresar una función f(x).
- Calcular dominio y recorrido.
- Ver intersecciones con los ejes X y Y.
- Evaluar la función en un valor específico de x.
- Graficar la función y resaltar el punto evaluado.

-----------------------------------
Requisitos
Antes de ejecutar el programa, asegúrate de tener instalado:

Python 3.8 o superior
Las siguientes librerías:

pip install sympy matplotlib

(Tkinter viene incluido en la mayoría de instalaciones de Python).

-----------------------------------
Estructura del Proyecto
El proyecto está dividido en 4 módulos, para facilitar el trabajo en equipo:

 analizador-funciones
 ┣  main.py          # Interfaz gráfica (Tkinter)
 ┣  funciones.py     # Lógica matemática y simbólica
 ┣  graficos.py      # Generación de gráficos con matplotlib
 ┣  utils.py         # Funciones auxiliares (validación de datos)
 ┗  README.md        # Documentación del proyecto

-----------------------------------
Ejecución
Para ejecutar el programa, abre una terminal en la carpeta del proyecto y corre:

python main.py
-----------------------------------
Ejemplos de Uso
Puedes probar con estas funciones:

Polinómica:
x**2 - 4
Valor opcional: 2

Racional:
(x**2 - 4)/(x - 2)
Valor opcional: 3

Trigonométrica:
sin(x)/x
Valor opcional: 1

Exponencial:
exp(x)
Valor opcional: 0

Raíz cuadrada:
sqrt(x-1)
Valor opcional: 2

-----------------------------------
Equipo de Desarrollo
El proyecto fue dividido en 4 partes, cada integrante desarrolló un módulo:

funciones.py → Análisis simbólico de funciones.
graficos.py → Generación de gráficos.
utils.py → Validación de datos.
main.py → Interfaz gráfica e integración.

-----------------------------------
Notas
Si al evaluar obtienes el mensaje:
"x = valor no pertenece al dominio de la función"
significa que intentaste evaluar en un punto donde la función no está definida (ejemplo: denominador igual a 0).
