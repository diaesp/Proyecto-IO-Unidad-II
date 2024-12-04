#Modelo de múltiples servidores con llegadas Poisson, tiempos de servicio arbitrarios y sin línea de espera,
import tkinter as tk
from tkinter import messagebox
from math import factorial

def caclulo():
    try:
        λ = float(tasa_llegada.get())
        μ = float(tasa_servicio.get())
        k = int(numero_canales.get())
        
        suma = sum((pow(λ / μ, i) / factorial(i)) for i in range(k + 1))
        Pk = (pow(λ / μ, k) / factorial(k)) / suma
        
        L = (λ / μ) * (1 - Pk)

        mostrar_resultados(Pk, L)
    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingresa valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error de cálculo", "Ocurrió una división por cero. Revisa las tasas de llegada y servicio.")

def mostrar_resultados(Pk, L):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados del modelo M/G/k con clientes bloqueados eliminados")
    ventana_resultados.config(bg="#f0f5f9")

    label_resultados = tk.Label(
        ventana_resultados, 
        text="Resultados del modelo M/G/k con clientes bloqueados eliminados", 
        font=("Arial", 10, "bold"),
        bg="#f0f5f9", fg="#33475b"
    )
    label_resultados.pack(pady=10)
    resultados_frame = tk.Frame(ventana_resultados, bg="#ffffff", bd=2, relief="ridge", padx=20, pady=10)
    resultados_frame.pack(padx=5, pady=10)

    resultados = [
        ("Probabilidad de bloqueo (Pk)", Pk),
        ("Número promedio de unidades en el sistema (L)", L)
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
    global tasa_llegada, tasa_servicio, numero_canales
    ventana = tk.Tk()
    ventana.title("M/G/k con clientes bloqueados eliminado")
    ventana.config(bg="#f7f9fc")

    header = tk.Label(ventana, text="M/G/k con clientes bloqueados eliminado", font=("Arial", 10, "bold"), bg="#f7f9fc", fg="#33475b")
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

    tk_poblacion = tk.Label(entrada_frame, text="Numero de canales (k):", font=("Arial", 10), bg="#f7f9fc", fg="#33475b")
    tk_poblacion.grid(row=2, column=0, pady=5, sticky="w")
    numero_canales = tk.Entry(entrada_frame, font=("Arial", 10), width=10)
    numero_canales.grid(row=2, column=1, pady=5)

    boton_calcular = tk.Button(
        ventana, text="Calcular", font=("Arial", 10, "bold"), bg="#FFB84D", fg="black", command=caclulo
    )
    boton_calcular.pack(pady=10)

    ventana.mainloop()

ventana()
