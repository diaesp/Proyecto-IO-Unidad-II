#Modelo de la mochila/equipo de vuelo/carga de contenedor
import tkinter as tk
from tkinter import messagebox

def mochila_con_repeticion(peso_maximo, pesos, beneficios):
    dp = [0] * (peso_maximo + 1)  
    seleccion = [0] * (peso_maximo + 1)  

    for w in range(1, peso_maximo + 1):
        for i in range(len(pesos)):
            if pesos[i] <= w:
                nuevo_ingreso = dp[w - pesos[i]] + beneficios[i]
                if nuevo_ingreso > dp[w]:
                    dp[w] = nuevo_ingreso
                    seleccion[w] = i + 1  

    w = peso_maximo
    asignaciones = [0] * len(pesos)
    while w > 0:
        if seleccion[w] == 0:
            break
        articulo = seleccion[w] - 1
        asignaciones[articulo] += 1
        w -= pesos[articulo]

    return dp[peso_maximo], asignaciones

def ejecutar_modelo():
    try:
        peso_maximo = int(entry_peso_maximo.get())
        pesos = list(map(int, entry_pesos.get().split(',')))
        beneficios = list(map(int, entry_beneficios.get().split(',')))

        if len(pesos) != len(beneficios):
            raise ValueError("Los pesos y beneficios deben tener el mismo número de elementos.")

        ingreso_maximo, asignaciones = mochila_con_repeticion(peso_maximo, pesos, beneficios)

        mostrar_resultados(ingreso_maximo, asignaciones)

    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

def mostrar_resultados(ingreso_maximo, asignaciones):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados del Modelo de la Mochila")
    ventana_resultados.config(bg="#f0f5f9")

    tk.Label(
        ventana_resultados,
        text="Resultados del Modelo de la Mochila",
        font=("Arial", 12, "bold"), bg="#f0f5f9", fg="#33475b"
    ).pack(pady=10)

    tk.Label(
        ventana_resultados,
        text=f"Ingreso máximo: {ingreso_maximo * 1000} dólares",
        font=("Arial", 10), bg="#ffffff", fg="#33475b"
    ).pack(pady=5)

    tk.Label(
        ventana_resultados,
        text=f"Unidades seleccionadas de cada artículo: {asignaciones}",
        font=("Arial", 10), bg="#ffffff", fg="#33475b"
    ).pack(pady=5)

    tk.Button(
        ventana_resultados, text="Cerrar", font=("Arial", 10), bg="#FFB84D", fg="black", 
        command=ventana_resultados.destroy
    ).pack(pady=10)

def ventana_principal():
    global entry_peso_maximo, entry_pesos, entry_beneficios

    ventana = tk.Tk()
    ventana.title("Modelo de la Mochila")
    ventana.config(bg="#f7f9fc")

    tk.Label(
        ventana,
        text="Modelo de la Mochila",
        font=("Arial", 12, "bold"), bg="#f7f9fc", fg="#33475b"
    ).pack(pady=10)

    frame_inputs = tk.Frame(ventana, bg="#f7f9fc")
    frame_inputs.pack(padx=10, pady=10)

    tk.Label(
        frame_inputs, text="Peso máximo:",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=0, column=0, pady=5, sticky="w")
    entry_peso_maximo = tk.Entry(frame_inputs, font=("Arial", 10), width=10)
    entry_peso_maximo.grid(row=0, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Pesos de los artículos (separados por comas):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=1, column=0, pady=5, sticky="w")
    entry_pesos = tk.Entry(frame_inputs, font=("Arial", 10), width=40)
    entry_pesos.grid(row=1, column=1, pady=5)

    tk.Label(
        frame_inputs, text="Beneficios de los artículos (separados por comas):",
        font=("Arial", 10), bg="#f7f9fc", fg="#33475b"
    ).grid(row=2, column=0, pady=5, sticky="w")
    entry_beneficios = tk.Entry(frame_inputs, font=("Arial", 10), width=40)
    entry_beneficios.grid(row=2, column=1, pady=5)

    tk.Button(
        ventana, text="Calcular", font=("Arial", 10, "bold"), bg="#FFB84D", fg="black", command=ejecutar_modelo
    ).pack(pady=10)

    ventana.mainloop()

ventana_principal()
