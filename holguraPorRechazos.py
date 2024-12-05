#determinacion de holguras por rechazos
import math
import tkinter as tk
from tkinter import messagebox


def binomial_prob(n, k, p):
    """Calcula la probabilidad binomial."""
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def calcular_politica_optima(p, costo_fijo, costo_marginal, costo_fallo, max_intentos, max_lote):
    dp = [[float('inf')] * (max_intentos + 1) for _ in range(max_lote + 1)]
    decision = [[-1] * (max_intentos + 1) for _ in range(max_lote + 1)]

    for l in range(max_lote + 1):
        dp[l][0] = costo_fallo

    for intentos in range(1, max_intentos + 1):
        for lote in range(1, max_lote + 1):
            costo_total = costo_fijo + lote * costo_marginal
            costo_esperado = costo_total

            for k in range(lote + 1):
                prob = binomial_prob(lote, k, p)
                if k > 0:  
                    costo_esperado += prob * 0  
                else: 
                    costo_esperado += prob * min(dp[l][intentos - 1] for l in range(1, max_lote + 1))

            dp[lote][intentos] = costo_esperado
            decision[lote][intentos] = lote

    politica_optima = []
    intentos = max_intentos
    while intentos > 0:
        mejor_lote = min(range(1, max_lote + 1), key=lambda l: dp[l][intentos])
        politica_optima.append(mejor_lote)
        intentos -= 1

    costo_minimo = min(dp[l][max_intentos] for l in range(1, max_lote + 1))
    return politica_optima[::-1], costo_minimo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Determinación de Holguras por Rechazo")
        self.geometry("500x400")
        self.configure(bg="#f7f9fc")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Determinación de Holguras por Rechazo", bg="#f7f9fc", font=("Arial", 10), fg="#33475b").pack(pady=10)

        self.p_entry = self.create_labeled_entry("Probabilidad de éxito (p):", "0.5")
        self.costo_fijo_entry = self.create_labeled_entry("Costo fijo por corrida:", "300")
        self.costo_marginal_entry = self.create_labeled_entry("Costo marginal por artículo:", "100")
        self.costo_fallo_entry = self.create_labeled_entry("Costo por fallo:", "1600")
        self.max_intentos_entry = self.create_labeled_entry("Máximo número de intentos:", "3")
        self.max_lote_entry = self.create_labeled_entry("Tamaño máximo del lote:", "4")
        tk.Button(self, text="Calcular Política Óptima", command=self.calcular, bg="#FFB84D", fg="black", font=("Arial", 9)).pack(pady=10)

    def create_labeled_entry(self, label, default_value):
        frame = tk.Frame(self, bg="#f7f9fc")
        frame.pack(pady=5)
        tk.Label(frame, text=label, bg="#f7f9fc", font=("Arial", 9), fg="#33475b").pack(side=tk.LEFT, padx=5)
        entry = tk.Entry(frame, width=20)
        entry.insert(0, default_value)
        entry.pack(side=tk.RIGHT, padx=5)
        return entry

    def calcular(self):
        try:
            p = float(self.p_entry.get())
            costo_fijo = float(self.costo_fijo_entry.get())
            costo_marginal = float(self.costo_marginal_entry.get())
            costo_fallo = float(self.costo_fallo_entry.get())
            max_intentos = int(self.max_intentos_entry.get())
            max_lote = int(self.max_lote_entry.get())

            politica, costo_minimo = calcular_politica_optima(p, costo_fijo, costo_marginal, costo_fallo, max_intentos, max_lote)

            self.mostrar_resultado(politica, costo_minimo)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def mostrar_resultado(self, politica, costo_minimo):
        resultado = tk.Toplevel(self)
        resultado.title("Resultado")
        resultado.geometry("400x300")
        resultado.configure(bg="#f0f5f9")

        tk.Label(resultado, text="Política Óptima", bg="#f0f5f9", font=("Arial", 10), fg="#33475b").pack(pady=10)
        tk.Label(resultado, text=f"Número de artículos por corrida: {politica}", bg="#f0f5f9", font=("Arial", 9), fg="#33475b").pack(pady=5)
        tk.Label(resultado, text=f"Costo total mínimo esperado: ${costo_minimo:.2f}", bg="#f0f5f9", font=("Arial", 9), fg="#33475b").pack(pady=5)

        tk.Button(resultado, text="Cerrar", command=resultado.destroy, bg="#FFB84D", fg="black", font=("Arial", 9)).pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
