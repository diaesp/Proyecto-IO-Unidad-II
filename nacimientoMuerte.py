#Esquema de nacimiento y muerte en sistema de colas (teorema de Little)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular():
    try:
        lmbda = float(entry_lambda.get())
        mu = float(entry_mu.get())
        capacity = int(entry_capacity.get())

        if lmbda <= 0 or mu <= 0 or capacity <= 0:
            raise ValueError("Todos los valores deben ser mayores que cero.")

        rho = lmbda / mu  
        P = []  

        P0 = 1 / sum([(rho**n) for n in range(capacity + 1)])
        P.append(P0)

        for n in range(1, capacity + 1):
            P.append((rho**n) * P0)

        Lq = sum([(n - 1) * P[n] for n in range(1, capacity + 1)])

        Wq = Lq / lmbda

        P_empty = P[0]

        utilization = 1 - P_empty

        resultado = (
            f"Resultados del sistema de colas:\n\n"
            f"Probabilidades de estado (Pn):\n"
            + "\n".join([f"P{n}: {P[n]:.4f}" for n in range(len(P))])
            + f"\n\nLongitud promedio de la cola (Lq): {Lq:.4f} pacientes"
            + f"\nTiempo promedio de espera en la cola (Wq): {Wq:.4f} horas"
            + f"\nProbabilidad de que el sistema esté vacío (P0): {P_empty:.4f} ({P_empty * 100:.2f}%)"
            + f"\nUtilización del sistema: {utilization:.4f} ({utilization * 100:.2f}%)"
        )

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, resultado)

    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

root = tk.Tk()
root.title("Esquema de Nacimiento y Muerte en Sistemas de Colas")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Tasa de llegada (λ):").grid(row=0, column=0, sticky=tk.W)
entry_lambda = ttk.Entry(frame, width=10)
entry_lambda.grid(row=0, column=1)

ttk.Label(frame, text="Tasa de servicio (μ):").grid(row=1, column=0, sticky=tk.W)
entry_mu = ttk.Entry(frame, width=10)
entry_mu.grid(row=1, column=1)

ttk.Label(frame, text="Capacidad máxima del sistema:").grid(row=2, column=0, sticky=tk.W)
entry_capacity = ttk.Entry(frame, width=10)
entry_capacity.grid(row=2, column=1)

btn_calcular = ttk.Button(frame, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

text_result = tk.Text(root, width=60, height=15, wrap="word")
text_result.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
