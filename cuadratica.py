#Programación cuadratica
import tkinter as tk
from tkinter import messagebox

def resolver_programacion_cuadratica():
    try:
        coef_x1 = float(entry_coef_x1.get())
        coef_x2 = float(entry_coef_x2.get())
        coef_x1_2 = float(entry_coef_x1_2.get())
        coef_x1x2 = float(entry_coef_x1x2.get())
        coef_x2_2 = float(entry_coef_x2_2.get())
        
        def funcion_objetivo(x1, x2):
            return coef_x1 * x1 + coef_x2 * x2 - coef_x1_2 * (x1**2) - coef_x1x2 * (x1 * x2) - coef_x2_2 * (x2**2)

        def cumple_restriccion(x1, x2):
            return x1 + 2 * x2 <= 2 and x1 >= 0 and x2 >= 0

        paso = 0.01  
        mejor_x1, mejor_x2 = 0, 0
        mejor_z = float('-inf')

        x1 = 0
        while x1 <= 2:
            x2 = 0
            while cumple_restriccion(x1, x2):
                z_actual = funcion_objetivo(x1, x2)
                if z_actual > mejor_z:
                    mejor_z = z_actual
                    mejor_x1, mejor_x2 = x1, x2
                x2 += paso
            x1 += paso

        mostrar_resultados(mejor_x1, mejor_x2, mejor_z)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def mostrar_resultados(x1_opt, x2_opt, z_opt):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultado Óptimo")
    ventana_resultados.configure(bg="#FDEBD0")  

    tk.Label(
        ventana_resultados, 
        text="Solución Óptima", 
        bg="#FDEBD0", fg="#8B4513", 
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Label(
        ventana_resultados, 
        text=f"x1 = {x1_opt:.2f}", 
        bg="#FFFFFF", fg="#8B4513", 
        font=("Arial", 12), 
        padx=10, pady=5
    ).pack(pady=5)

    tk.Label(
        ventana_resultados, 
        text=f"x2 = {x2_opt:.2f}", 
        bg="#FFFFFF", fg="#8B4513", 
        font=("Arial", 12), 
        padx=10, pady=5
    ).pack(pady=5)

    tk.Label(
        ventana_resultados, 
        text=f"z = {z_opt:.2f}", 
        bg="#FFFFFF", fg="#8B4513", 
        font=("Arial", 12), 
        padx=10, pady=5
    ).pack(pady=5)

    tk.Button(
        ventana_resultados, 
        text="Cerrar", 
        bg="#F5B041", fg="black", 
        font=("Arial", 10, "bold"), 
        command=ventana_resultados.destroy
    ).pack(pady=10)

ventana = tk.Tk()
ventana.title("Programación Cuadrática")
ventana.configure(bg="#FDEBD0") 

tk.Label(
    ventana, 
    text="Maximizar: z = 4x1 + 6x2 - 2x1² - 2x1x2 - 2x2²", 
    bg="#FDEBD0", fg="#8B4513", 
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Label(
    ventana, 
    text="Sujeto a: x1 + 2x2 <= 2 y x1, x2 >= 0", 
    bg="#FDEBD0", fg="#8B4513", 
    font=("Arial", 10)
).pack(pady=5)

frame_funcion_objetivo = tk.Frame(ventana, bg="#FDEBD0")
frame_funcion_objetivo.pack(padx=10, pady=5)

tk.Label(frame_funcion_objetivo, text="Coeficiente de x1:", bg="#FDEBD0", fg="#8B4513").grid(row=0, column=0)
entry_coef_x1 = tk.Entry(frame_funcion_objetivo)
entry_coef_x1.grid(row=0, column=1)

tk.Label(frame_funcion_objetivo, text="Coeficiente de x2:", bg="#FDEBD0", fg="#8B4513").grid(row=1, column=0)
entry_coef_x2 = tk.Entry(frame_funcion_objetivo)
entry_coef_x2.grid(row=1, column=1)

tk.Label(frame_funcion_objetivo, text="Coef. de x1^2:", bg="#FDEBD0", fg="#8B4513").grid(row=2, column=0)
entry_coef_x1_2 = tk.Entry(frame_funcion_objetivo)
entry_coef_x1_2.grid(row=2, column=1)

tk.Label(frame_funcion_objetivo, text="Coef. de x1*x2:", bg="#FDEBD0", fg="#8B4513").grid(row=3, column=0)
entry_coef_x1x2 = tk.Entry(frame_funcion_objetivo)
entry_coef_x1x2.grid(row=3, column=1)

tk.Label(frame_funcion_objetivo, text="Coef. de x2^2:", bg="#FDEBD0", fg="#8B4513").grid(row=4, column=0)
entry_coef_x2_2 = tk.Entry(frame_funcion_objetivo)
entry_coef_x2_2.grid(row=4, column=1)

tk.Button(
    ventana, text="Resolver", command=resolver_programacion_cuadratica,
    bg="#F5B041", fg="black", font=("Arial", 12, "bold")
).pack(pady=20)

ventana.mainloop()
