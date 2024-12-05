# Modelo de reemplazo de equipo
import tkinter as tk
from tkinter import messagebox


class ResultadosVentana(tk.Toplevel):
    def __init__(self, parent, resultado_texto):
        super().__init__(parent)
        self.title("Resultados de Optimización")
        self.geometry("600x400")
        self.configure(bg="#FFF4E6")  

        tk.Label(self, text="Resultados", font=("Arial", 12, "bold"), bg="#FFF4E6", fg="black").pack(pady=10)

        resultados_text = tk.Text(self, wrap="word", bg="white", fg="black", font=("Arial", 10), relief="flat")
        resultados_text.insert("end", resultado_texto)
        resultados_text.config(state="disabled")  
        resultados_text.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Button(self, text="Cerrar", command=self.destroy, bg="#FFAB73", fg="black", font=("Arial", 10), relief="flat").pack(pady=10)


class ProgramacionDinamicaVentana(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Optimización con Programación Dinámica")
        self.geometry("800x600")
        self.configure(bg="#FFF4E6") 

        tk.Label(self, text="Optimización con Programación Dinámica", font=("Arial", 14, "bold"), bg="#FFF4E6", fg="black").pack(pady=10)

        tk.Label(self, text="Ingrese los ingresos (separados por coma):", bg="#FFF4E6", fg="black", font=("Arial", 10)).pack(pady=5)
        self.ingresos_entry = tk.Entry(self, width=80, bg="#FFF4E6", fg="black")
        self.ingresos_entry.pack()

        tk.Label(self, text="Ingrese los costos de operación (separados por coma):", bg="#FFF4E6", fg="black", font=("Arial", 10)).pack(pady=5)
        self.costos_entry = tk.Entry(self, width=80, bg="#FFF4E6", fg="black")
        self.costos_entry.pack()

        tk.Label(self, text="Ingrese los valores de desecho (separados por coma):", bg="#FFF4E6", fg="black", font=("Arial", 10)).pack(pady=5)
        self.valores_entry = tk.Entry(self, width=80, bg="#FFF4E6", fg="black")
        self.valores_entry.pack()

        tk.Label(self, text="Costo de una nueva máquina (en miles):", bg="#FFF4E6", fg="black", font=("Arial", 10)).pack(pady=5)
        self.costo_maquina_entry = tk.Entry(self, width=20, bg="#FFF4E6", fg="black")
        self.costo_maquina_entry.pack()

        tk.Label(self, text="Número de años:", bg="#FFF4E6", fg="black", font=("Arial", 10)).pack(pady=5)
        self.n_anios_entry = tk.Entry(self, width=10, bg="#FFF4E6", fg="black")
        self.n_anios_entry.pack()

        tk.Label(self, text="Edad inicial de la máquina:", bg="#FFF4E6", fg="black", font=("Arial", 10)).pack(pady=5)
        self.edad_inicial_entry = tk.Entry(self, width=10, bg="#FFF4E6", fg="black")
        self.edad_inicial_entry.pack()

        tk.Button(self, text="Resolver", command=self.resolver, bg="#FFAB73", fg="black", font=("Arial", 10), relief="flat").pack(pady=20)

    def resolver(self):
        try:
            ingresos = list(map(float, self.ingresos_entry.get().split(',')))
            costos_operacion = list(map(float, self.costos_entry.get().split(',')))
            valores_desecho = list(map(float, self.valores_entry.get().split(',')))
            costo_nueva_maquina = float(self.costo_maquina_entry.get())
            n_anios = int(self.n_anios_entry.get())
            edad_inicial = int(self.edad_inicial_entry.get())
            n_edades = len(ingresos)

            if len(costos_operacion) != n_edades or len(valores_desecho) != n_edades:
                raise ValueError("Todos los vectores deben tener el mismo tamaño.")
            
            beneficios = [[0] * n_anios for _ in range(n_edades)]
            decisiones = [[None] * n_anios for _ in range(n_edades)]

            for etapa in range(n_anios - 1, -1, -1):
                for edad in range(n_edades):
                    if etapa == n_anios - 1:
                        if edad == n_edades - 1:
                            beneficio_reemplazo = (
                                ingresos[0] + valores_desecho[edad] + valores_desecho[1]
                                - costos_operacion[0] - costo_nueva_maquina
                            )
                            beneficios[edad][etapa] = beneficio_reemplazo
                            decisiones[edad][etapa] = "R"
                        else:
                            beneficio_conservar = (
                                ingresos[edad] - costos_operacion[edad] + valores_desecho[edad + 1]
                            )
                            beneficio_reemplazo = (
                                ingresos[0] + valores_desecho[edad] + valores_desecho[1]
                                - costos_operacion[0] - costo_nueva_maquina
                            )
                            if beneficio_conservar >= beneficio_reemplazo:
                                beneficios[edad][etapa] = beneficio_conservar
                                decisiones[edad][etapa] = "K"
                            else:
                                beneficios[edad][etapa] = beneficio_reemplazo
                                decisiones[edad][etapa] = "R"
                    else:
                        if edad < n_edades - 1:
                            beneficio_conservar = (
                                ingresos[edad] - costos_operacion[edad] + beneficios[edad + 1][etapa + 1]
                            )
                        else:
                            beneficio_conservar = float('-inf')
                        beneficio_reemplazo = (
                            ingresos[0] + valores_desecho[edad] - costos_operacion[0]
                            - costo_nueva_maquina + beneficios[1][etapa + 1]
                        )
                        if beneficio_conservar >= beneficio_reemplazo:
                            beneficios[edad][etapa] = beneficio_conservar
                            decisiones[edad][etapa] = "K"
                        else:
                            beneficios[edad][etapa] = beneficio_reemplazo
                            decisiones[edad][etapa] = "R"

            edad_actual = edad_inicial
            solucion = []
            beneficio_total = beneficios[edad_actual][0]
            for etapa in range(n_anios):
                decision = decisiones[edad_actual][etapa]
                solucion.append(decision)
                if decision == "R":
                    edad_actual = 1
                else:
                    edad_actual += 1

            resultado_texto = (
                f"Beneficio total: ${beneficio_total * 1000:.1f}\n"
                f"Política óptima: {solucion}\n"
            )
            ResultadosVentana(self, resultado_texto)

        except Exception as e:
            messagebox.showerror("Error", f"Error al resolver el problema: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    ventana = ProgramacionDinamicaVentana(root)
    root.mainloop()
