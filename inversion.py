#Modelo de Inversion
import tkinter as tk
from tkinter import messagebox

def calcular_inversion():
    try:
        capital_inicial = float(entry_capital_inicial.get())
        inversiones = [float(entry_inversion[i].get()) for i in range(4)]
        tasas_first = [float(entry_tasa_first[i].get()) for i in range(4)]
        bonos_first = [float(entry_bono_first[i].get()) for i in range(4)]
        tasas_second = [float(entry_tasa_second[i].get()) for i in range(4)]
        bonos_second = [float(entry_bono_second[i].get()) for i in range(4)]

        resultado = calcular_inversion_dinamica(
            capital_inicial, inversiones, tasas_first, bonos_first, tasas_second, bonos_second
        )

        mostrar_resultado(resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def mostrar_resultado(resultado):
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultado del Modelo de Inversión")
    ventana_resultado.config(bg="#f3f8ff")  
    ventana_resultado.geometry("400x200")

    tk.Label(
        ventana_resultado,
        text="Resultado de la Inversión",
        bg="#f3f8ff",
        font=("Arial", 14, "bold"),
        fg="#33475b"
    ).pack(pady=10)

    tk.Label(
        ventana_resultado,
        text=f"El capital máximo acumulado al final de los 4 años es:\n\n${resultado:.2f}",
        bg="#f3f8ff",
        font=("Arial", 12),
        fg="#5a5a5a",
        justify="center"
    ).pack(pady=10)

    tk.Button(
        ventana_resultado,
        text="Cerrar",
        command=ventana_resultado.destroy,
        bg="#ffb380",
        fg="black",
        font=("Arial", 10)
    ).pack(pady=10)

def calcular_inversion_dinamica(capital_inicial, inversiones, tasas_first, bonos_first, tasas_second, bonos_second):
    n = len(tasas_first)
    dp_first = [0] * (n + 1)
    dp_second = [0] * (n + 1)

    dp_first[0] = dp_second[0] = capital_inicial

    for i in range(1, n + 1):
        dp_first[i] = max(
            dp_first[i - 1] * (1 + tasas_first[i - 1]),
            dp_second[i - 1] * (1 + tasas_first[i - 1]),
        ) + inversiones[i - 1] * (1 + bonos_first[i - 1])

        dp_second[i] = max(
            dp_first[i - 1] * (1 + tasas_second[i - 1]),
            dp_second[i - 1] * (1 + tasas_second[i - 1]),
        ) + inversiones[i - 1] * (1 + bonos_second[i - 1])

    return max(dp_first[n], dp_second[n])

ventana = tk.Tk()
ventana.title("Modelo de Inversión Dinámica")
ventana.config(bg="#f9f9f9")  

frame_datos = tk.Frame(ventana, bg="#f9f9f9")
frame_datos.pack(padx=20, pady=10)

tk.Label(frame_datos, text="Capital inicial ($):", bg="#f9f9f9").grid(row=0, column=0, sticky="w", pady=5)
entry_capital_inicial = tk.Entry(frame_datos, width=10)
entry_capital_inicial.grid(row=0, column=1, pady=5)
entry_capital_inicial.insert(0, "4000")

tk.Label(frame_datos, text="Inversiones anuales ($):", bg="#f9f9f9").grid(row=1, column=0, sticky="w", pady=5)
entry_inversion = []
for i in range(4):
    entry = tk.Entry(frame_datos, width=8)
    entry.grid(row=1, column=i + 1, pady=5)
    entry.insert(0, "2000")
    entry_inversion.append(entry)

labels_bancos = [
    ("Tasas First Bank (%):", entry_tasa_first := []),
    ("Bonos First Bank (%):", entry_bono_first := []),
    ("Tasas Second Bank (%):", entry_tasa_second := []),
    ("Bonos Second Bank (%):", entry_bono_second := []),
]

for idx, (label_text, entry_list) in enumerate(labels_bancos, start=2):
    tk.Label(frame_datos, text=label_text, bg="#f9f9f9").grid(row=idx, column=0, sticky="w", pady=5)
    for i in range(4):
        entry = tk.Entry(frame_datos, width=8)
        entry.grid(row=idx, column=i + 1, pady=5)
        if "First" in label_text:
            entry.insert(0, f"{0 if i == 0 else 0.018 - 0.001 * i}" if "Bonos" in label_text else "0.08")
        else:
            entry.insert(0, f"{0 if i == 0 else 0.023 - 0.001 * i}" if "Bonos" in label_text else "0.078")
        entry_list.append(entry)

boton_calcular = tk.Button(
    ventana,
    text="Calcular Capital Máximo",
    command=calcular_inversion,
    bg="#ffb380",  
    fg="black",
    font=("Arial", 10),
)
boton_calcular.pack(pady=20)

ventana.mainloop()
