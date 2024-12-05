# Ganadora en Las Vegas
import tkinter as tk
from tkinter import messagebox

def calcular_politica_optima_vegas(fichas_iniciales, prob_ganar, jugadas, meta):
    dp = [[0] * (jugadas + 1) for _ in range(meta + 1)]
    politica = [[0] * (jugadas + 1) for _ in range(meta + 1)]

    for x in range(meta + 1):
        dp[x][0] = 1 if x >= meta else 0

    for j in range(1, jugadas + 1):
        for x in range(meta + 1):
            max_prob = 0
            mejor_apuesta = 0

            for a in range(x + 1):  
                if x + a <= meta and x - a >= 0:
                    prob = (
                        prob_ganar * dp[x + a][j - 1]  
                        + (1 - prob_ganar) * dp[x - a][j - 1] 
                    )
                    if prob > max_prob:
                        max_prob = prob
                        mejor_apuesta = a

            dp[x][j] = max_prob
            politica[x][j] = mejor_apuesta

    probabilidad_maxima = dp[fichas_iniciales][jugadas]
    decisiones = []
    fichas = fichas_iniciales

    for j in range(jugadas, 0, -1):
        apuesta = politica[fichas][j]
        decisiones.append(apuesta)
        if apuesta > 0:
            if dp[fichas + apuesta][j - 1] > dp[fichas - apuesta][j - 1]:
                fichas += apuesta  
            else:
                fichas -= apuesta 

    return decisiones[::-1], probabilidad_maxima


def mostrar_resultado():
    try:
        fichas_iniciales = int(entry_fichas_iniciales.get())
        prob_ganar = float(entry_probabilidad.get())
        jugadas = int(entry_jugadas.get())
        meta = int(entry_meta.get())

        decisiones, probabilidad = calcular_politica_optima_vegas(fichas_iniciales, prob_ganar, jugadas, meta)

        ventana_resultado = tk.Toplevel(ventana)
        ventana_resultado.title("Resultado")
        ventana_resultado.config(bg="#f2fcff") 
        resultado = f"Política óptima (número de fichas a apostar por jugada): {decisiones}\n"
        resultado += f"Probabilidad máxima de éxito: {probabilidad:.4f}"

        label_resultado = tk.Label(ventana_resultado, text=resultado, bg="#f2fcff", font=("Arial", 12))
        label_resultado.pack(padx=10, pady=20)

        btn_cerrar = tk.Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, bg="#ffb380", fg="black")  
        btn_cerrar.pack(pady=10)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Ganadora en Las Vegas - Programación Dinámica")
ventana.config(bg="#f2fcff") 

label_fichas_iniciales = tk.Label(ventana, text="Fichas iniciales:", bg="#f2fcff")
label_fichas_iniciales.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_fichas_iniciales = tk.Entry(ventana)
entry_fichas_iniciales.grid(row=0, column=1, padx=10, pady=10)

label_probabilidad = tk.Label(ventana, text="Probabilidad de ganar:", bg="#f2fcff")
label_probabilidad.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_probabilidad = tk.Entry(ventana)
entry_probabilidad.grid(row=1, column=1, padx=10, pady=10)

label_jugadas = tk.Label(ventana, text="Número de jugadas:", bg="#f2fcff")
label_jugadas.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_jugadas = tk.Entry(ventana)
entry_jugadas.grid(row=2, column=1, padx=10, pady=10)

label_meta = tk.Label(ventana, text="Meta de fichas:", bg="#f2fcff")
label_meta.grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_meta = tk.Entry(ventana)
entry_meta.grid(row=3, column=1, padx=10, pady=10)

btn_calcular = tk.Button(ventana, text="Calcular Política Óptima", command=mostrar_resultado, bg="#ffb380", fg="black")  
btn_calcular.grid(row=4, column=0, columnspan=2, pady=20)

ventana.mainloop()
