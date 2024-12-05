#Programación separable
import tkinter as tk
from tkinter import messagebox

def resolver_programacion_separable(c1, c2, r1, r2, b):
    def cumple_restriccion(x1, x2):
        return c1 * x1 + c2 * (x2**r2) <= b

    def funcion_objetivo(x1, x2):
        return x1 + (x2**r1)

    mejor_x1, mejor_x2 = 0, 0
    mejor_z = float('-inf')

    paso = 0.01
    x1 = 0
    while c1 * x1 <= b:
        x2 = 0
        while cumple_restriccion(x1, x2):
            z_actual = funcion_objetivo(x1, x2)
            if z_actual > mejor_z:
                mejor_z = z_actual
                mejor_x1, mejor_x2 = x1, x2
            x2 += paso
        x1 += paso

    return mejor_x1, mejor_x2, mejor_z

def ejecutar_resolucion():
    try:
        c1 = float(entry_c1.get())
        c2 = float(entry_c2.get())
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())
        b = float(entry_b.get())

        x1_opt, x2_opt, z_opt = resolver_programacion_separable(c1, c2, r1, r2, b)

        mostrar_resultados(x1_opt, x2_opt, z_opt)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

def mostrar_resultados(x1_opt, x2_opt, z_opt):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultado Óptimo")
    ventana_resultados.configure(bg="#FDEBD0")  

    tk.Label(
        ventana_resultados, 
        text="Solución Óptima", 
        bg="#FDEBD0", fg="#8B4513", 
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Label(
        ventana_resultados, 
        text=f"x1 = {x1_opt:.2f}", 
        bg="#FFFFFF", fg="#8B4513", 
        font=("Arial", 12), 
        padx=10, pady=5
    ).pack(pady=5)

    tk.Label(
        ventana_resultados, 
        text=f"x2 = {x2_opt:.2f}", 
        bg="#FFFFFF", fg="#8B4513", 
        font=("Arial", 12), 
        padx=10, pady=5
    ).pack(pady=5)

    tk.Label(
        ventana_resultados, 
        text=f"z = {z_opt:.2f}", 
        bg="#FFFFFF", fg="#8B4513", 
        font=("Arial", 12), 
        padx=10, pady=5
    ).pack(pady=5)

    tk.Button(
        ventana_resultados, 
        text="Cerrar", 
        bg="#F5B041", fg="black", 
        font=("Arial", 10, "bold"), 
        command=ventana_resultados.destroy
    ).pack(pady=10)

ventana = tk.Tk()
ventana.title("Resolución de Programación Separable")
ventana.configure(bg="#FDEBD0")  

def crear_label(texto, fila):
    tk.Label(ventana, text=texto, bg="#FDEBD0", fg="#8B4513", font=("Arial", 10)).grid(row=fila, column=0, pady=5, sticky="e")

def crear_entry(fila):
    entry = tk.Entry(ventana, font=("Arial", 10), width=15)
    entry.grid(row=fila, column=1, padx=10, pady=5)
    return entry

crear_label("Coeficiente de x1 (c1):", 0)
entry_c1 = crear_entry(0)

crear_label("Coeficiente de x2 (c2):", 1)
entry_c2 = crear_entry(1)

crear_label("Exponente de x2 en la función objetivo (r1):", 2)
entry_r1 = crear_entry(2)

crear_label("Exponente de x2 en la restricción (r2):", 3)
entry_r2 = crear_entry(3)

crear_label("Constante del lado derecho de la restricción (b):", 4)
entry_b = crear_entry(4)

boton_calcular = tk.Button(
    ventana, text="Calcular", command=ejecutar_resolucion,
    bg="#F5B041", fg="black", font=("Arial", 12, "bold")
)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()
