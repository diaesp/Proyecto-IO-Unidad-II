import tkinter as tk
from tkinter import messagebox

entry_lambda = None
entry_mu = None
entry_servicios = None

def calcular_resultados():
    try:
        lambda_ = float(entry_lambda.get())
        mu = float(entry_mu.get())
        num_servicios = int(entry_servicios.get())
        
        if lambda_ >= mu:
            messagebox.showerror("Error", "La tasa de llegada (λ) debe ser menor que la tasa de servicio (μ).")
            return
        ρ = lambda_ / (num_servicios * mu)  # Utilización del servidor
        P0 = 1 - ρ  # Probabilidad de que no haya clientes en el sistema
        Lq = (lambda_ ** 2) / (num_servicios * mu * (mu - lambda_))  # Número promedio de clientes en la cola
        L = lambda_ / (mu - lambda_)  # Número promedio de clientes en el sistema
        Wq = Lq / lambda_  # Tiempo promedio de espera en la cola
        W = L / lambda_  # Tiempo promedio en el sistema
        mostrar_resultados(lambda_, mu, num_servicios, ρ, P0, Lq, L, Wq, W)

    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingresa valores numéricos válidos.")

def mostrar_resultados(lambda_, mu, num_servicios, ρ, P0, Lq, L, Wq, W):

    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados M/M/1")
    label_resultados = tk.Label(ventana_resultados, text="Resultados del modelo M/M/1", font=("Arial", 14))
    label_resultados.pack(pady=10)

    resultados = (
        f"Tasa de llegada (λ): {lambda_} clientes/segundo\n"
        f"Tasa de servicio (μ): {mu} clientes/segundo\n"
        f"Número de servicios: {num_servicios}\n"
        f"Utilización del servidor (ρ): {ρ:.2f}\n"
        f"Probabilidad de que no haya clientes (P₀): {P0:.2f}\n"
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
    global entry_lambda, entry_mu, entry_servicios
    ventana_principal = tk.Tk()
    ventana_principal.title("Modelo M/M/1")
    label_lambda = tk.Label(ventana_principal, text="Introduce la tasa de llegada (λ):", font=("Arial", 12))
    label_lambda.pack(pady=10)
    entry_lambda = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_lambda.pack(pady=5)

    label_mu = tk.Label(ventana_principal, text="Introduce la tasa de servicio (μ):", font=("Arial", 12))
    label_mu.pack(pady=10)
    entry_mu = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_mu.pack(pady=5)

    label_servicios = tk.Label(ventana_principal, text="Introduce el número de servicios:", font=("Arial", 12))
    label_servicios.pack(pady=10)
    entry_servicios = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_servicios.pack(pady=5)

    boton_calcular = tk.Button(ventana_principal, text="Calcular", font=("Arial", 12), bg="#FFB84D", fg="black", command=calcular_resultados)
    boton_calcular.pack(pady=20)

    ventana_principal.mainloop()

crear_ventana_principal()
