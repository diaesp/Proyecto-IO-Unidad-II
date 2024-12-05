#Distribución de científicos entre grupos de investigación
import tkinter as tk
from tkinter import messagebox, ttk

def calcular_asignacion():
    try:
        cientificos_disponibles = 2
        tabla_str = entry_tabla.get("1.0", tk.END).strip()

        tabla = [list(map(float, fila.split(','))) for fila in tabla_str.splitlines()]
        
        if len(tabla) != 3 or not all(len(fila) == 3 for fila in tabla):
            raise ValueError("Debe ingresar una tabla de 3 filas y 3 columnas.")

        mejor_comb = None
        prob_minima = float('inf')
        
        for c1 in range(cientificos_disponibles + 1):
            for c2 in range(cientificos_disponibles - c1 + 1):
                c3 = cientificos_disponibles - c1 - c2  # Restantes para el equipo 3
                
                probabilidad = (
                    tabla[0][c1] *  # Probabilidad de fracaso del equipo 1 con c1 científicos
                    tabla[1][c2] *  # Probabilidad de fracaso del equipo 2 con c2 científicos
                    tabla[2][c3]    # Probabilidad de fracaso del equipo 3 con c3 científicos
                )
                
                if probabilidad < prob_minima:
                    prob_minima = probabilidad
                    mejor_comb = (c1, c2, c3)

        mostrar_resultados(mejor_comb, prob_minima)

    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

def mostrar_resultados(mejor_comb, prob_minima):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados de la Distribución")
    ventana_resultados.config(bg="#f7f9fc")
    
    ttk.Label(
        ventana_resultados, 
        text="Resultados de la Distribución de Científicos", 
        font=("Arial", 12, "bold")
    ).pack(pady=10)
    
    frame_resultados = ttk.LabelFrame(ventana_resultados, text="Distribución Detallada", padding=(10, 10))
    frame_resultados.pack(padx=10, pady=10, fill="both", expand=True)
    
    ttk.Label(frame_resultados, text="Equipo", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(frame_resultados, text="Científicos Asignados", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    
    for i, asignados in enumerate(mejor_comb):
        ttk.Label(frame_resultados, text=f"Equipo {i+1}", font=("Arial", 10)).grid(row=i+1, column=0, padx=5, pady=5)
        ttk.Label(frame_resultados, text=f"{asignados}", font=("Arial", 10)).grid(row=i+1, column=1, padx=5, pady=5)
    
    frame_probabilidad = ttk.LabelFrame(ventana_resultados, text="Resumen", padding=(10, 10))
    frame_probabilidad.pack(padx=10, pady=10, fill="x")
    
    ttk.Label(frame_probabilidad, text=f"Probabilidad mínima de fracaso: {prob_minima:.5f}", font=("Arial", 10, "bold")).pack(pady=5)
    
    tk.Button(
        ventana_resultados, 
        text="Cerrar", 
        font=("Arial", 10, "bold"), 
        bg="#FFB84D", 
        fg="black", 
        command=ventana_resultados.destroy
    ).pack(pady=10)

def ventana_principal():
    global entry_tabla
    ventana = tk.Tk()
    ventana.title("Distribución de Científicos entre Grupos")
    ventana.config(bg="#f7f9fc")
    
    ttk.Label(
        ventana, 
        text="Distribución de Científicos entre Grupos de Investigación", 
        font=("Arial", 12, "bold"),
        background="#f7f9fc", foreground="#33475b"
    ).pack(pady=10)
    
    frame_inputs = ttk.Frame(ventana, padding=(10, 10))
    frame_inputs.pack(padx=10, pady=10)
    
    ttk.Label(
        frame_inputs, 
        text="Tabla de Probabilidades (separar columnas por comas y filas por líneas):", 
        font=("Arial", 10), 
        foreground="#33475b"
    ).grid(row=0, column=0, pady=5, sticky="w")
    
    entry_tabla = tk.Text(frame_inputs, font=("Arial", 10), width=40, height=10)
    entry_tabla.grid(row=1, column=0, pady=5)
    
    tk.Button(
        ventana, 
        text="Calcular Distribución", 
        font=("Arial", 10, "bold"), 
        bg="#FFB84D", 
        fg="black", 
        command=calcular_asignacion
    ).pack(pady=10)
    
    ventana.mainloop()

ventana_principal()
