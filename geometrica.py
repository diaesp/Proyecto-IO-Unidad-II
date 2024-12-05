#Programacion Geometrica
import tkinter as tk
from tkinter import messagebox

class ProgramacionGeometrica:
    def __init__(self, master):
        self.master = master
        self.master.title("Resolución de Programación Geométrica")
        self.master.configure(bg='#FFE0B2')  

        self.button_style = {'bg': '#FFB74D', 'fg': 'white', 'width': 15, 'height': 2, 'bd': 0}  
        self.response_style = {'bg': '#FFE0B2', 'fg': 'black', 'width': 30, 'height': 2}  

        self.obj_lineal1_label = tk.Label(self.master, text="Coeficiente lineal de x1:", bg='#FFE0B2')
        self.obj_lineal1_label.pack(pady=5)
        self.obj_lineal1 = tk.Entry(self.master)
        self.obj_lineal1.pack(pady=5)

        self.obj_lineal2_label = tk.Label(self.master, text="Coeficiente lineal de x2:", bg='#FFE0B2')
        self.obj_lineal2_label.pack(pady=5)
        self.obj_lineal2 = tk.Entry(self.master)
        self.obj_lineal2.pack(pady=5)

        self.obj_cuadratico1_label = tk.Label(self.master, text="Coeficiente cuadrático de x1:", bg='#FFE0B2')
        self.obj_cuadratico1_label.pack(pady=5)
        self.obj_cuadratico1 = tk.Entry(self.master)
        self.obj_cuadratico1.pack(pady=5)

        self.obj_cuadratico2_label = tk.Label(self.master, text="Coeficiente cuadrático de x2:", bg='#FFE0B2')
        self.obj_cuadratico2_label.pack(pady=5)
        self.obj_cuadratico2 = tk.Entry(self.master)
        self.obj_cuadratico2.pack(pady=5)

        self.restriccion_label = tk.Label(self.master, text="Restricción: x1 + x2 >= 1", bg='#FFE0B2')
        self.restriccion_label.pack(pady=5)

        self.restriccion2_label = tk.Label(self.master, text="Restricción: x1^2 + x2^2 <= 4", bg='#FFE0B2')
        self.restriccion2_label.pack(pady=5)

        self.calcular_button = tk.Button(self.master, text="Calcular", command=self.calcular, **self.button_style)
        self.calcular_button.pack(pady=20)

    def calcular(self):
        try:
            a1 = float(self.obj_lineal1.get())
            a2 = float(self.obj_lineal2.get())
            b1 = float(self.obj_cuadratico1.get())
            b2 = float(self.obj_cuadratico2.get())

           
            x1, x2 = 0.5, 0.5
            tasa_aprendizaje = 0.01  
            tolerancia = 1e-6
            iteraciones_maximas = 1000
            for i in range(iteraciones_maximas):
                gradiente_x1 = 2 * b1 * x1 + a1
                gradiente_x2 = 4 * b2 * x2 + a2

                x1 -= tasa_aprendizaje * gradiente_x1
                x2 -= tasa_aprendizaje * gradiente_x2

                if x1 + x2 < 1:  
                    x1 = 0.5  
                    x2 = 0.5
                    break

                if x1**2 + x2**2 > 4: 
                    x1 = 0.5  
                    x2 = 0.5
                    break

                if abs(gradiente_x1) < tolerancia and abs(gradiente_x2) < tolerancia:
                    break

            resultado = a1 * x1 + a2 * x2 + b1 * x1**2 + b2 * x2**2

            resultado_texto = f"Valor óptimo de Z: {resultado:.2f}\nSolución óptima:\n x1 = {x1:.2f}, x2 = {x2:.2f}"

            self.mostrar_respuesta(resultado_texto)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def mostrar_respuesta(self, respuesta):
        # Ventana de respuesta
        respuesta_ventana = tk.Toplevel(self.master)
        respuesta_ventana.title("Resultado")
        respuesta_ventana.configure(bg='#FFE0B2')  

        respuesta_label = tk.Label(respuesta_ventana, text=respuesta, **self.response_style)
        respuesta_label.pack(padx=20, pady=10, fill='both', expand=True)  

        cerrar_button = tk.Button(respuesta_ventana, text="Cerrar", command=respuesta_ventana.destroy, **self.button_style)
        cerrar_button.pack(pady=10)

        respuesta_ventana.geometry(f"300x200+{self.master.winfo_x() + 50}+{self.master.winfo_y() + 50}") 
        respuesta_ventana.resizable(False, False)  
        respuesta_ventana.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramacionGeometrica(root)
    root.mainloop()
