#Programacion Convexa
import tkinter as tk
from tkinter import messagebox

def evaluar_funcion_objetivo(funcion_str, variables):
    return eval(funcion_str, {}, variables)

def calcular_gradiente(funcion_str, variables, var_keys, h=1e-6):
    gradiente = []
    for key in var_keys:
        vars_copy = variables.copy()
        vars_copy[key] += h
        f1 = evaluar_funcion_objetivo(funcion_str, vars_copy)
        vars_copy[key] -= 2 * h
        f2 = evaluar_funcion_objetivo(funcion_str, vars_copy)
        gradiente.append((f1 - f2) / (2 * h))
    return gradiente

def resolver_programacion_convexa(funcion_objetivo, restricciones, valores_iniciales, tipo_optimizacion, max_iter=100, tol=1e-6, alpha=0.01):
    variables = {f"x{i+1}": valores_iniciales[i] for i in range(len(valores_iniciales))}
    var_keys = list(variables.keys())
    restricciones_parsed = [r.split("=") for r in restricciones.split(";")]

    for _ in range(max_iter):
        grad = calcular_gradiente(funcion_objetivo, variables, var_keys)
        if tipo_optimizacion == "Minimización":
            grad = [-g for g in grad]
        
        for i, key in enumerate(var_keys):
            variables[key] += alpha * grad[i]
        
        for restriccion in restricciones_parsed:
            lhs, rhs = restriccion
            lhs_val = eval(lhs, {}, variables)
            rhs_val = eval(rhs, {}, variables)
            error = lhs_val - rhs_val
            for key in var_keys:
                variables[key] -= alpha * error / len(var_keys)
        
        error_grad = max(abs(g) for g in grad)
        error_restricciones = max(abs(eval(lhs, {}, variables) - eval(rhs, {}, variables)) for lhs, rhs in restricciones_parsed)
        if error_grad < tol and error_restricciones < tol:
            break

    return variables

def obtener_datos():
    try:
        funcion_objetivo = entry_funcion_objetivo.get()
        restricciones = entry_restricciones.get()
        valores_iniciales = list(map(float, entry_valores_iniciales.get().split(",")))
        tipo_optimizacion = var_optimizacion.get()

        solucion = resolver_programacion_convexa(funcion_objetivo, restricciones, valores_iniciales, tipo_optimizacion)

        mostrar_resultados(solucion)
    except Exception as e:
        messagebox.showerror("Error", f"Error en los datos de entrada: {e}")

def mostrar_resultados(solucion):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultado Óptimo")
    ventana_resultados.configure(bg="#FDEBD0")
    tk.Label(ventana_resultados, text="Solución Óptima", bg="#FDEBD0", fg="#8B4513", font=("Arial", 14, "bold")).pack(pady=10)

    for key, valor in solucion.items():
        tk.Label(ventana_resultados, text=f"{key} = {valor:.4f}", bg="#FFFFFF", fg="#8B4513", font=("Arial", 12)).pack(pady=5)

    tk.Button(ventana_resultados, text="Cerrar", bg="#F5B041", fg="black", font=("Arial", 10, "bold"), command=ventana_resultados.destroy).pack(pady=10)

ventana = tk.Tk()
ventana.title("Programación Convexa")
ventana.configure(bg="#FDEBD0")

tk.Label(ventana, text="Función Objetivo:", bg="#FDEBD0", fg="#8B4513", font=("Arial", 10, "bold")).pack(pady=5)
entry_funcion_objetivo = tk.Entry(ventana, width=50)
entry_funcion_objetivo.pack(pady=5)

tk.Label(ventana, text="Restricciones separadas por ';':", bg="#FDEBD0", fg="#8B4513", font=("Arial", 10, "bold")).pack(pady=5)
entry_restricciones = tk.Entry(ventana, width=50)
entry_restricciones.pack(pady=5)

tk.Label(ventana, text="Valores Iniciales:", bg="#FDEBD0", fg="#8B4513", font=("Arial", 10, "bold")).pack(pady=5)
entry_valores_iniciales = tk.Entry(ventana, width=50)
entry_valores_iniciales.pack(pady=5)

tk.Label(ventana, text="Tipo de Optimización:", bg="#FDEBD0", fg="#8B4513", font=("Arial", 10, "bold")).pack(pady=5)
var_optimizacion = tk.StringVar(value="Maximización")
tk.Radiobutton(ventana, text="Minimización", variable=var_optimizacion, value="Minimización", bg="#FDEBD0").pack()
tk.Radiobutton(ventana, text="Maximización", variable=var_optimizacion, value="Maximización", bg="#FDEBD0").pack()

tk.Button(ventana, text="Resolver", command=obtener_datos, bg="#F5B041", fg="black", font=("Arial", 12, "bold")).pack(pady=20)

ventana.mainloop()
