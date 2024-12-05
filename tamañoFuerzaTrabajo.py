#Modelo de tamaño de la fuerza de trabajo
import tkinter as tk
from tkinter import messagebox

memo = {}
decisiones = {}

def costo_exceso(trabajadores_actuales, minimo_requerido):
    return 300 * max(0, trabajadores_actuales - minimo_requerido)

def costo_contratacion(trabajadores_actuales, trabajadores_previos):
    if trabajadores_actuales > trabajadores_previos:
        return 400 + 200 * (trabajadores_actuales - trabajadores_previos)
    return 0

def calcular_costo(semana, trabajadores_previos, requerimientos, max_trabajadores):
    if semana == len(requerimientos):
        return 0  

    estado = (semana, trabajadores_previos)
    if estado in memo:
        return memo[estado]

    costo_minimo = float('inf')
    mejor_decision = -1

    for trabajadores_actuales in range(requerimientos[semana], max_trabajadores + 1):
        costo_actual = (
            costo_exceso(trabajadores_actuales, requerimientos[semana]) +
            costo_contratacion(trabajadores_actuales, trabajadores_previos) +
            calcular_costo(semana + 1, trabajadores_actuales, requerimientos, max_trabajadores)
        )

        if costo_actual < costo_minimo:
            costo_minimo = costo_actual
            mejor_decision = trabajadores_actuales

    memo[estado] = costo_minimo
    decisiones[estado] = mejor_decision

    return costo_minimo

def ejecutar_modelo():
    try:
        requerimientos = list(map(int, entry_requerimientos.get().split(',')))
        max_trabajadores = int(entry_max_trabajadores.get())

        memo.clear()
        decisiones.clear()

        costo_total = calcular_costo(0, 0, requerimientos, max_trabajadores)

        plan_optimo = []
        trabajadores_previos = 0
        for semana in range(len(requerimientos)):
            trabajadores_actuales = decisiones[(semana, trabajadores_previos)]
            plan_optimo.append(trabajadores_actuales)
            trabajadores_previos = trabajadores_actuales

        mostrar_resultados(costo_total, plan_optimo)

    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingresa valores válidos.")
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

def mostrar_resultados(costo_total, plan_optimo):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados del Modelo de Tamaño de la Fuerza de Trabajo")
    ventana_resultados.config(bg="#f0f5f9")

    tk.Label(
        ventana_resultados,
        text="Resultados del Modelo de Tamaño de la Fuerza de Trabajo",
        font=("Arial", 12, "bold"), bg="#f0f5f9", fg="#33475b"
    ).pack(pady=10)

    tk.Label(
        ventana_resultados,
        text=f"Costo total mínimo: {costo_total}",
        font=("Arial", 10), bg="#ffffff", fg="#33475b"
    ).pack(pady=5)

    tk.Label(
        ventana_resultados,
        text="Plan óptimo de contratación por semana:",
        font=("Arial", 10, "bold"), bg="#f0f5f9", fg="#33475b"
    ).pack(pady=10)

    for semana, trabajadores in enumerate(plan_optimo, start=1):
        tk.Label(
            ventana_resultados,
            text=f"Semana {semana}: {trabajadores} trabajadores",
            font=("Arial", 10), bg="#ffffff", fg="#33475b"
        ).pack(pady=2)

    tk.Button(
        ventana_resultados, text="Cerrar", font=("Arial", 10), bg="#FFB84D", fg="black", 
        command=ventana_resultados.destroy
    ).pack(pady=10)

def ventana_principal():
    global entry_requerimientos, entry_max_trabajadores

    ventana = tk.Tk()
    ventana.title("Modelo de Tamaño de la Fuerza de Trabajo")
    ventana.config(bg="#f7f9fc")

    tk.Label(
        ventana,
        text="Modelo de Tamaño de la Fuerza de Trabajo",
        font=("Arial", 12, "bold"), bg="#f7f9fc", fg="#33475b"
    ).pack(pady=10)

    frame_inputs = tk.Frame(ventana, bg="#f7f9fc")
    frame_inputs.pack(padx=10, pady=10)

    tk.Label(
        frame_inputs, text="Requerimientos semanales (separados por comas):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=0, column=0, pady=5, sticky="w")
    entry_requerimientos = tk.Entry(frame_inputs, font=("Arial", 10), width=40)
    entry_requerimientos.grid(row=0, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Máximo de trabajadores:",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=1, column=0, pady=5, sticky="w")
    entry_max_trabajadores = tk.Entry(frame_inputs, font=("Arial", 10), width=10)
    entry_max_trabajadores.grid(row=1, column=1, pady=5)

    tk.Button(
        ventana, text="Calcular", font=("Arial", 10, "bold"), bg="#FFB84D", fg="black", command=ejecutar_modelo
    ).pack(pady=10)

    ventana.mainloop()

ventana_principal()
