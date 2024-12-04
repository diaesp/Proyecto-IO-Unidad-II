#Modelo de línea de espera con un servidor y con llegadas Poisson y tiempos de servicio exponenciales
import tkinter as tk
from tkinter import messagebox

entry_lambda = None
entry_mu = None

def calcular_resultados():
    try:
        λ = float(entry_lambda.get())
        mu = float(entry_mu.get())
        
        if λ >= mu:
            messagebox.showerror("Error", "La tasa de llegada (λ) debe ser menor que la tasa de servicio (μ).")
            return

        P0 = 1 - (λ/mu)  # Probabilidad de que no haya clientes en el sistema
        Lq = (λ ** 2) / (mu * (mu - λ))  # Número promedio de clientes en la cola
        L = Lq + (λ/mu)  # Número promedio de clientes en el sistema
        Wq = Lq / λ  # Tiempo promedio de espera en la cola
        W = Wq + (1/mu)  # Tiempo promedio en el sistema
        Pw = λ/mu #Probabilidad que una unidad no tenga que esperar

        mostrar_resultados(λ, mu, P0, Lq, L, Wq, W, Pw)

    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingresa valores numéricos válidos.")

def mostrar_resultados(lambda_, mu, P0, Lq, L, Wq, W, Pw):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title(" Resultados")

    label_resultados = tk.Label(ventana_resultados, text=" Resultados", font=("Arial", 14))
    label_resultados.pack(pady=10)

    resultados = (
        f"Tasa de llegada (λ): {lambda_} \n"
        f"Tasa de servicio (μ): {mu} \n"
        f"Probabilidad de que no haya clientes (P₀): {P0:.2f}\n"
        f"Número promedio de clientes en la cola (Lq): {Lq:.2f}\n"
        f"Número promedio de clientes en el sistema (L): {L:.2f}\n"
        f"Tiempo promedio de espera en la cola (Wq): {Wq:.2f} minutos\n"
        f"Tiempo promedio en el sistema (W): {W:.2f} minutos\n"
        f"Probabilidad de que una unidad que llega no tenga que esperar (Pw): {Pw:.2f} \n"
    )
    
    label_resultados_texto = tk.Label(ventana_resultados, text=resultados, font=("Arial", 12))
    label_resultados_texto.pack(padx=20, pady=10)

    boton_cerrar = tk.Button(ventana_resultados, text="Cerrar", font=("Arial", 12), bg="#FFB84D", fg="black", command=ventana_resultados.destroy)
    boton_cerrar.pack(pady=10)

def crear_ventana_principal():
    global entry_lambda, entry_mu

    ventana_principal = tk.Tk()
    ventana_principal.title("Modelo de línea de espera de canal único con llegadas Poisson y tiempos de servicio exponenciales")
    
    label_lambda = tk.Label(ventana_principal, text="Introduce la tasa de llegada (λ):", font=("Arial", 12))
    label_lambda.pack(pady=10)
    entry_lambda = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_lambda.pack(pady=5)

    label_mu = tk.Label(ventana_principal, text="Introduce la tasa de servicio (μ):", font=("Arial", 12))
    label_mu.pack(pady=10)
    entry_mu = tk.Entry(ventana_principal, font=("Arial", 12))
    entry_mu.pack(pady=5)

    boton_calcular = tk.Button(ventana_principal, text="Calcular", font=("Arial", 12), bg="#FFB84D", fg="black", command=calcular_resultados)
    boton_calcular.pack(pady=20)

    ventana_principal.mainloop()

crear_ventana_principal()
