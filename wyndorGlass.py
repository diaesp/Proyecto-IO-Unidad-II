#Problema de la Wyndor Glass Company
import tkinter as tk
from tkinter import messagebox

def resolver_programacion_lineal(coef_objetivo, restricciones, limites):

    max_z = 0
    max_x1 = 0
    max_x2 = 0

    max_x1_valor = int(limites[0] // restricciones[0][0]) + 1  # Calcular un rango amplio para x1
    max_x2_valor = int(limites[1] // restricciones[1][1]) + 1  # Calcular un rango amplio para x2

    for x1 in range(max_x1_valor):
        for x2 in range(max_x2_valor):
            cumple_restricciones = True
            for i in range(len(restricciones)):
                if restricciones[i][0] * x1 + restricciones[i][1] * x2 > limites[i]:
                    cumple_restricciones = False
                    break
            if cumple_restricciones:
                z = coef_objetivo[0] * x1 + coef_objetivo[1] * x2
                if z > max_z:
                    max_z = z
                    max_x1 = x1
                    max_x2 = x2
    return max_z, max_x1, max_x2

def ejecutar_modelo():
    try:
        coef_objetivo = list(map(int, entry_coef_objetivo.get().split(",")))
        restricciones = [
            list(map(int, entry_restriccion_1.get().split(","))),
            list(map(int, entry_restriccion_2.get().split(","))),
            list(map(int, entry_restriccion_3.get().split(","))),
        ]
        limites = list(map(int, entry_limites.get().split(",")))

        resultado, x1_optimo, x2_optimo = resolver_programacion_lineal(coef_objetivo, restricciones, limites)

        mostrar_resultados(resultado, x1_optimo, x2_optimo)

    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingresa valores válidos.")
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

def mostrar_resultados(resultado, x1_optimo, x2_optimo):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados del Problema de Programación Lineal")
    ventana_resultados.config(bg="#f0f5f9")

    tk.Label(
        ventana_resultados,
        text="Resultados del Problema de Programación Lineal",
        font=("Arial", 12, "bold"), bg="#f0f5f9", fg="#33475b"
    ).pack(pady=10)

    tk.Label(
        ventana_resultados,
        text=f"Valor óptimo de Z: {resultado}",
        font=("Arial", 10), bg="#ffffff", fg="#33475b"
    ).pack(pady=5)

    tk.Label(
        ventana_resultados,
        text=f"x1 óptimo: {x1_optimo}, x2 óptimo: {x2_optimo}",
        font=("Arial", 10), bg="#ffffff", fg="#33475b"
    ).pack(pady=5)

    tk.Button(
        ventana_resultados, text="Cerrar", font=("Arial", 10), bg="#FFB84D", fg="black",
        command=ventana_resultados.destroy
    ).pack(pady=10)

def ventana_principal():
    global entry_coef_objetivo, entry_restriccion_1, entry_restriccion_2, entry_restriccion_3, entry_limites

    ventana = tk.Tk()
    ventana.title("Modelo de Programación Lineal")
    ventana.config(bg="#f7f9fc")

    tk.Label(
        ventana,
        text="Modelo de Programación Lineal",
        font=("Arial", 12, "bold"), bg="#f7f9fc", fg="#33475b"
    ).pack(pady=10)

    frame_inputs = tk.Frame(ventana, bg="#f7f9fc")
    frame_inputs.pack(padx=10, pady=10)

    tk.Label(
        frame_inputs, text="Coeficientes de la función objetivo (ejemplo: 3,5):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=0, column=0, pady=5, sticky="w")
    entry_coef_objetivo = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
    entry_coef_objetivo.grid(row=0, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Restricción 1 (ejemplo: 1,0):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=1, column=0, pady=5, sticky="w")
    entry_restriccion_1 = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
    entry_restriccion_1.grid(row=1, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Restricción 2 (ejemplo: 0,2):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=2, column=0, pady=5, sticky="w")
    entry_restriccion_2 = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
    entry_restriccion_2.grid(row=2, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Restricción 3 (ejemplo: 3,2):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=3, column=0, pady=5, sticky="w")
    entry_restriccion_3 = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
    entry_restriccion_3.grid(row=3, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Límites de las restricciones (ejemplo: 4,12,18):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=4, column=0, pady=5, sticky="w")
    entry_limites = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
    entry_limites.grid(row=4, column=1, pady=5)

    tk.Button(
        ventana, text="Calcular", font=("Arial", 10, "bold"), bg="#FFB84D", fg="black", command=ejecutar_modelo
    ).pack(pady=10)

    ventana.mainloop()

ventana_principal()
