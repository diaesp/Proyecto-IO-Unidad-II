#Modelos de línea de espera con fuentes finitas
import tkinter as tk
from tkinter import messagebox
from math import factorial

def caclulo():
    try:
        λ = float(tasa_llegada.get())
        μ = float(tasa_servicio.get())
        N = int(tamaño_poblacion.get())
        
        P0 = 1 / sum((factorial(N) / (factorial(N - n) * pow(μ / λ, n))) for n in range(N + 1))
        Lq = N - ((λ + μ) / λ) * (1 - P0)
        L = Lq + (1 - P0)
        Wq = Lq / ((N - L) * λ)
        W = Wq + (1 / μ)
        Pw = 1 - P0

        mostrar_resultados(P0, Lq, L, Wq, W, Pw)
    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingresa valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error de cálculo", "Ocurrió una división por cero. Revisa las tasas de llegada y servicio.")

def mostrar_resultados(P0, Lq, L, Wq, W, Pw):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados del modelo M/M/1 con población finita")
    ventana_resultados.config(bg="#f0f5f9")

    label_resultados = tk.Label(
        ventana_resultados, 
        text="Resultados del modelo M/M/1 con población finita", 
        font=("Arial", 10, "bold"),
        bg="#f0f5f9", fg="#33475b"
    )
    label_resultados.pack(pady=10)

    resultados_frame = tk.Frame(ventana_resultados, bg="#ffffff", bd=2, relief="ridge", padx=20, pady=10)
    resultados_frame.pack(padx=5, pady=10)

    resultados = [
        ("Probabilidad que no haya unidades en el sistema (P0)", P0),
        ("Número promedio de unidades en la línea de espera (Lq)", Lq),
        ("Número promedio de unidades en el sistema (L)", L),
        ("Tiempo promedio en la línea de espera (Wq)", Wq),
        ("Tiempo promedio en el sistema (W)", W),
        ("Probabilidad de que una unidad que llega espere (Pw)", Pw)
    ]

    for label, value in resultados:
        tk.Label(resultados_frame, text=f"{label}: ", font=("Arial", 10, "bold"), anchor="w", bg="#ffffff", fg="#33475b").grid(sticky="w")
        tk.Label(resultados_frame, text=f"{value:.2f}", font=("Arial", 10), bg="#ffffff", fg="#33475b").grid(sticky="w", pady=5)

    boton_cerrar = tk.Button(
        ventana_resultados, text="Cerrar", font=("Arial", 10), bg="#FFB84D", fg="black", 
        command=ventana_resultados.destroy
    )
    boton_cerrar.pack(pady=10)

def ventana():
    global tasa_llegada, tasa_servicio, tamaño_poblacion
    ventana = tk.Tk()
    ventana.title("M/M/1 con población finita")
    ventana.config(bg="#f7f9fc")

    header = tk.Label(ventana, text="Modelo M/M/1 con población finita", font=("Arial", 10, "bold"), bg="#f7f9fc", fg="#33475b")
    header.pack(pady=15)

    entrada_frame = tk.Frame(ventana, bg="#f7f9fc")
    entrada_frame.pack(padx=20, pady=10)

    label_llegada = tk.Label(entrada_frame, text="Tasa de llegada (λ):", font=("Arial", 10), bg="#f7f9fc", fg="#33475b")
    label_llegada.grid(row=0, column=0, pady=5, sticky="w")
    tasa_llegada = tk.Entry(entrada_frame, font=("Arial", 10), width=10)
    tasa_llegada.grid(row=0, column=1, pady=5)

    label_servicio = tk.Label(entrada_frame, text="Tasa de servicio (μ):", font=("Arial", 10), bg="#f7f9fc", fg="#33475b")
    label_servicio.grid(row=1, column=0, pady=5, sticky="w")
    tasa_servicio = tk.Entry(entrada_frame, font=("Arial", 10), width=10)
    tasa_servicio.grid(row=1, column=1, pady=5)

    label_poblacion = tk.Label(entrada_frame, text="Tamaño de la población (N):", font=("Arial", 10), bg="#f7f9fc", fg="#33475b")
    label_poblacion.grid(row=2, column=0, pady=5, sticky="w")
    tamaño_poblacion = tk.Entry(entrada_frame, font=("Arial", 10), width=10)
    tamaño_poblacion.grid(row=2, column=1, pady=5)

    boton_calcular = tk.Button(
        ventana, text="Calcular", font=("Arial", 10, "bold"), bg="#FFB84D", fg="black", command=caclulo
    )
    boton_calcular.pack(pady=10)

    ventana.mainloop()

ventana()
