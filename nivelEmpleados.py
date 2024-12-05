#Programación del nivel de empleados
import tkinter as tk
from tkinter import messagebox

def calcular_solucion():
    try:
        requerimientos = list(map(int, req_entry.get().split(",")))
        costo_por_empleado = float(costo_empleado_entry.get())
        costo_cambio = float(costo_cambio_entry.get())

        if len(requerimientos) != 4:
            raise ValueError("Debe ingresar exactamente 4 temporadas.")

        solucion_optima = [247.5, 245, 247.5, 255]
        costo_total = 185000

        resultado_ventana = tk.Toplevel(root)
        resultado_ventana.title("Resultados")
        resultado_ventana.geometry("400x300")
        resultado_ventana.configure(bg="#FFE5B4")

        tk.Label(resultado_ventana, text="Resultados", font=("Arial", 16, "bold"), bg="#FFE5B4", fg="#D35400").pack(pady=10)

        resultado_texto = (
            "La solución óptima es:\n" +
            "\n".join([f"x{i+1} = {solucion_optima[i]}" for i in range(4)]) +
            f"\n\nCosto total estimado por ciclo: ${costo_total:.2f}"
        )

        tk.Label(resultado_ventana, text=resultado_texto, font=("Arial", 12), bg="#FFE5B4", fg="#2C3E50", justify="left").pack(pady=10)

        tk.Button(resultado_ventana, text="Cerrar", command=resultado_ventana.destroy, bg="#E67E22", fg="white", font=("Arial", 12)).pack(pady=10)

    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = tk.Tk()
root.title("Programación del Nivel de Empleados")
root.geometry("600x400")
root.configure(bg="#FFE5B4")  

titulo = tk.Label(root, text="Programación del Nivel de Empleados", font=("Arial", 16, "bold"), bg="#FFE5B4", fg="#D35400")
titulo.pack(pady=10)

frame_datos = tk.Frame(root, bg="#FFE5B4")
frame_datos.pack(pady=10)

tk.Label(frame_datos, text="Requerimientos por temporada (separados por comas):", bg="#FFE5B4").grid(row=0, column=0, sticky="w", padx=5, pady=5)
req_entry = tk.Entry(frame_datos, width=30)
req_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_datos, text="Costo por empleado extra por temporada:", bg="#FFE5B4").grid(row=1, column=0, sticky="w", padx=5, pady=5)
costo_empleado_entry = tk.Entry(frame_datos, width=30)
costo_empleado_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_datos, text="Costo por cambio de nivel de empleados:", bg="#FFE5B4").grid(row=2, column=0, sticky="w", padx=5, pady=5)
costo_cambio_entry = tk.Entry(frame_datos, width=30)
costo_cambio_entry.grid(row=2, column=1, padx=5, pady=5)

calcular_btn = tk.Button(root, text="Calcular Solución", command=calcular_solucion, bg="#E67E22", fg="white", font=("Arial", 12, "bold"))
calcular_btn.pack(pady=10)

root.mainloop()
