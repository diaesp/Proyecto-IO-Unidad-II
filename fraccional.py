#Programacion Fraccional
import tkinter as tk
from tkinter import messagebox

def calcular_inversion():
    try:
        C1 = float(entry_costo_fijo.get())  # Costo fijo por camión
        C2 = float(entry_costo_variable.get())  # Costo variable por unidad transportada
        demanda_total = float(entry_demanda.get())  # Demanda total de productos
        capacidad_camion = float(entry_capacidad.get())  # Capacidad de cada camión

        num_camiones = (demanda_total + capacidad_camion - 1) // capacidad_camion

        def costo_total(x):
            if x <= 0:
                return float('inf')  
            return (C1 / x) + C2

        productos_por_camion_optimo = None
        costo_minimo = float('inf')

        for productos_por_camion in range(1, int(capacidad_camion) + 1):
            costo = costo_total(productos_por_camion)
            if costo < costo_minimo:
                costo_minimo = costo
                productos_por_camion_optimo = productos_por_camion

        resultado = f"Cantidad óptima de productos por camión: {productos_por_camion_optimo}\n"
        resultado += f"Costo total por unidad de producto transportado: {costo_minimo:.2f}\n"
        resultado += f"Total de camiones necesarios: {num_camiones}"

        ventana_resultado = tk.Toplevel(ventana)
        ventana_resultado.title("Resultado")
        ventana_resultado.geometry("400x300")
        ventana_resultado.config(bg="#f7d8b8")  

        label_resultado = tk.Label(ventana_resultado, text=resultado, font=("Arial", 10), bg="#f7d8b8")
        label_resultado.pack(pady=20)

        btn_cerrar = tk.Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, bg="#f57f28", fg="white", font=("Arial", 10))
        btn_cerrar.pack(pady=10)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Optimización de Transporte de Productos")
ventana.geometry("500x400")
ventana.config(bg="#f7d8b8")  

tk.Label(ventana, text="Costo fijo por camión ($):", bg="#f7d8b8", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_costo_fijo = tk.Entry(ventana, font=("Arial", 10))
entry_costo_fijo.grid(row=0, column=1, padx=10, pady=10)
entry_costo_fijo.insert(0, "1000")

tk.Label(ventana, text="Costo variable por unidad ($):", bg="#f7d8b8", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_costo_variable = tk.Entry(ventana, font=("Arial", 10))
entry_costo_variable.grid(row=1, column=1, padx=10, pady=10)
entry_costo_variable.insert(0, "5")

tk.Label(ventana, text="Demanda total de productos:", bg="#f7d8b8", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_demanda = tk.Entry(ventana, font=("Arial", 10))
entry_demanda.grid(row=2, column=1, padx=10, pady=10)
entry_demanda.insert(0, "1500")

tk.Label(ventana, text="Capacidad de cada camión:", bg="#f7d8b8", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_capacidad = tk.Entry(ventana, font=("Arial", 10))
entry_capacidad.grid(row=3, column=1, padx=10, pady=10)
entry_capacidad.insert(0, "200")

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular Capital Máximo", command=calcular_inversion, bg="#f57f28", fg="white", font=("Arial", 10))
boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop()
