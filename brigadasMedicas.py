#Distribución de brigadas médicas entre países
import tkinter as tk
from tkinter import ttk, messagebox


def calcular_asignacion():
    try:
        brigadas_disponibles = int(entry_brigadas.get())
        
        tabla_str = entry_tabla.get("1.0", tk.END).strip()
        tabla = [list(map(int, fila.split(','))) for fila in tabla_str.splitlines()]
        
        num_paises = len(tabla)
        num_brigadas = len(tabla[0])
        
        if brigadas_disponibles > num_brigadas * num_paises:
            raise ValueError("Hay más brigadas disponibles que las posibles asignaciones.")
        
        mejor_beneficio = -1
        mejor_asignacion = []
        
        def backtracking(asignacion_actual, pais_actual, brigadas_restantes):
            nonlocal mejor_beneficio, mejor_asignacion
            
            if pais_actual == num_paises:
                beneficio_total = sum(
                    tabla[i][asignacion_actual[i]] for i in range(len(asignacion_actual))
                )
                if beneficio_total > mejor_beneficio:
                    mejor_beneficio = beneficio_total
                    mejor_asignacion = asignacion_actual[:]
                return
            
            for b in range(num_brigadas + 1):  
                if brigadas_restantes >= b:
                    asignacion_actual.append(b)
                    backtracking(asignacion_actual, pais_actual + 1, brigadas_restantes - b)
                    asignacion_actual.pop()
        
        backtracking([], 0, brigadas_disponibles)
        
        mostrar_resultados(mejor_asignacion, mejor_beneficio, tabla)
    except ValueError as ve:
        messagebox.showerror("Error de entrada", str(ve))
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un problema: {e}")


def mostrar_resultados(asignacion, beneficio_total, tabla):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados de Asignación")
    ventana_resultados.config(bg="#f7f9fc")
    
    ttk.Label(
        ventana_resultados, 
        text="Resultados de la Asignación de Brigadas Médicas", 
        font=("Arial", 12, "bold")
    ).pack(pady=10)
    
    frame_resultados = ttk.LabelFrame(ventana_resultados, text="Resultados Detallados", padding=(10, 10))
    frame_resultados.pack(padx=10, pady=10, fill="both", expand=True)
    
    ttk.Label(frame_resultados, text="País", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(frame_resultados, text="Brigadas Asignadas", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(frame_resultados, text="Beneficio Obtenido", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
    
    for i, brigadas in enumerate(asignacion):
        beneficio = tabla[i][brigadas]
        ttk.Label(frame_resultados, text=f"País {i+1}", font=("Arial", 10)).grid(row=i+1, column=0, padx=5, pady=5)
        ttk.Label(frame_resultados, text=f"{brigadas}", font=("Arial", 10)).grid(row=i+1, column=1, padx=5, pady=5)
        ttk.Label(frame_resultados, text=f"{beneficio}", font=("Arial", 10)).grid(row=i+1, column=2, padx=5, pady=5)
    
    frame_total = ttk.LabelFrame(ventana_resultados, text="Resumen", padding=(10, 10))
    frame_total.pack(padx=10, pady=10, fill="x")
    
    ttk.Label(frame_total, text=f"Beneficio Total: {beneficio_total} mil años-persona", font=("Arial", 10, "bold")).pack(pady=5)
    
    tk.Button(
        ventana_resultados, 
        text="Cerrar", 
        font=("Arial", 10, "bold"), 
        bg="#FFB84D", 
        fg="black", 
        command=ventana_resultados.destroy
    ).pack(pady=10)



def ventana_principal():
    global entry_brigadas, entry_tabla
    ventana = tk.Tk()
    ventana.title("Asignación de Brigadas Médicas")
    ventana.config(bg="#f7f9fc")
    
    tk.Label(
        ventana, 
        text="Asignación de Brigadas Médicas entre Países", 
        font=("Arial", 12, "bold"), 
        bg="#f7f9fc", fg="#33475b"
    ).pack(pady=10)
    
    frame_brigadas = ttk.LabelFrame(ventana, text="Información General", padding=(10, 10))
    frame_brigadas.pack(padx=10, pady=10, fill="x")
    
    tk.Label(frame_brigadas, text="Brigadas Disponibles:", font=("Arial", 10)).grid(row=0, column=0, pady=5, sticky="w")
    entry_brigadas = tk.Entry(frame_brigadas, font=("Arial", 10), width=10)
    entry_brigadas.grid(row=0, column=1, pady=5)
    
    frame_tabla = ttk.LabelFrame(ventana, text="Matriz de Beneficios", padding=(10, 10))
    frame_tabla.pack(padx=10, pady=10, fill="both", expand=True)
    
    tk.Label(frame_tabla, text="Ingrese los beneficios para cada país y brigada (separados por comas):", font=("Arial", 10)).pack(pady=5, anchor="w")
    entry_tabla = tk.Text(frame_tabla, font=("Arial", 10), width=50, height=10)
    entry_tabla.pack(pady=5)
    
    tk.Button(
        ventana, text="Calcular Asignación", font=("Arial", 10, "bold"), bg="#FFB84D", fg="black", command=calcular_asignacion
    ).pack(pady=10)
    
    ventana.mainloop()


ventana_principal()
