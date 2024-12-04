import tkinter as tk
from tkinter import messagebox
import math

entry_lambda = None
entry_mu = None
entry_servidores = None

def calcular_resultados():
    try:
        lambda_ = float(entry_lambda.get())
        mu = float(entry_mu.get())
        c = int(entry_servidores.get())
        
        if lambda_ >= c * mu:
            messagebox.showerror("Error", "La tasa de llegada (λ) debe ser menor que la capacidad del sistema (c * μ).")
            return
        ρ = lambda_ / mu  # Utilización del sistema
        P0 = calcular_P0(lambda_, mu, c)  # Probabilidad de que no haya clientes en el sistema
        Lq = (P0 * ((lambda_ / mu) ** c) * ρ) / (math.factorial(c) * ((1 - ρ) ** 2))  # Número promedio de clientes en la cola
        L = Lq + lambda_ / mu  # Número promedio de clientes en el sistema
        Wq = Lq / lambda_  # Tiempo promedio de espera en la cola
        W = Wq + (1 / mu)  # Tiempo promedio en el sistema

        mostrar_resultados(lambda_, mu, c, ρ, P0, Lq, L, Wq, W)

    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingresa valores numéricos válidos.")

def calcular_P0(lambda_, mu, c):
    sumatoria = sum((lambda_ / mu) ** n / math.factorial(n) for n in range(c))
    P0 = 1 / (sumatoria + ((lambda_ / mu) ** c) / (math.factorial(c) * (1 - (lambda_ / (c * mu)))))
    return P0

def mostrar_resultados(lambda_, mu, c, ρ, P0, Lq, L, Wq, W):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados M/M/c")
    label_resultados = tk.Label(ventana_resultados, text="Resultados del modelo M/M/c", font=("Arial", 14))
    label_resultados.pack(pady=10)

    resultados = (
        f"Tasa de llegada (λ): {lambda_} clientes/segundo\n"
        f"Tasa de servicio (μ): {mu} clientes/segundo\n"
        f"Número de servidores (c): {c}\n"
        f"Utilización del sistema (ρ): {ρ:.2f}\n"
        f"Probabilidad de que no haya clientes (P₀): {P0:.4f}\n"
        f"Número promedio de clientes en la cola (Lq): {Lq:.2f}\n"
        f"Número promedio de clientes en el sistema (L): {L:.2f}\n"
        f"Tiempo promedio de espera en la cola (Wq): {Wq:.2f} segundos\n"
        f"Tiempo promedio en el sistema (W): {W:.2f} segundos\n"
    )
    
    label_resultados_texto = tk.Label(ventana_resultados, text=resultados, font=("Arial", 12))
    label_resultados_texto.pack(padx=20, pady=10)

    boton_cerrar = tk.Button(ventana_resultados, text="Cerrar", font=("Arial", 12), bg="#FFB84D", fg="black", command=ventana_resultados.destroy)
    boton_cerrar.pack(pady=10)

def crear_ventana_principal():
    global entry_lambda, entry_mu, entry_servidores

    ventana_principal = tk.Tk()
    ventana_principal.title("Modelo M/M/c")
    
    label_lambda = tk.Label(ventana_principal, text="Introduce la tasa de llegada (λ):", font=("Arial", 12))
    label_lambda.pack(pady=10)
    entry_lambda = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_lambda.pack(pady=5)

    label_mu = tk.Label(ventana_principal, text="Introduce la tasa de servicio (μ):", font=("Arial", 12))
    label_mu.pack(pady=10)
    entry_mu = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_mu.pack(pady=5)

    label_servidores = tk.Label(ventana_principal, text="Introduce el número de servidores (c):", font=("Arial", 12))
    label_servidores.pack(pady=10)
    entry_servidores = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_servidores.pack(pady=5)

    boton_calcular = tk.Button(ventana_principal, text="Calcular", font=("Arial", 12), bg="#FFB84D", fg="black", command=calcular_resultados)
    boton_calcular.pack(pady=20)

    ventana_principal.mainloop()

crear_ventana_principal()
