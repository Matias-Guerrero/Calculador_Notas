import tkinter as tk
import tkinter.font as tkFont
import variables
import pandas as pd

## Funciones
def guardarNotas():
    if variables.contadorWidgets == 0 or variables.datos is None: return
    
    df_notas = pd.DataFrame(columns=["N° Nota", "Nota", "Porcentaje(%)"], index=range(variables.contadorWidgets + 1))
    
    for indice in range(0, variables.contadorWidgets):
        
        datos = [indice + 1, variables.datos[0][indice], variables.datos[1][indice] * 100]
        
        df_notas.iloc[indice] = datos
        
    datos = ["Promedio", variables.datos[2], None]
    df_notas.iloc[variables.contadorWidgets] = datos
    
    print(df_notas)
    df_notas.to_excel("notas.xlsx", index=False)
        
        

def calcularNota():
    if variables.contadorWidgets == 0: return
    
    variables.datos = []

    notas = []
    porcentajes = []
    sumaPorcentaje = 0

    for porcentaje in variables.listaPorcentajes:
        try:
            porcentajes.append(int(porcentaje.get()) / 100)
            sumaPorcentaje += porcentajes[-1]
        except:
            print("Problema 1")
            actualizarSalida("Informacion Incorrecta")
            return

    for nota in variables.listaNotas:
        try:
            notas.append(float(nota.get()))
        except:
            print("Problema 2")
            actualizarSalida("Informacion Incorrecta")
            return
        
        for indice in range(0, len(notas)):
            if notas[indice] < 1 or notas[indice] > 7:
                actualizarSalida("Notas Incorrectas")
                return 
    
    promedio = 0

    if sumaPorcentaje is float or sumaPorcentaje != 1:
        actualizarSalida("Porcentaje Incorrecto")
        return
    else:
        for indice in range(0, len(notas)):
            promedio += (notas[indice] * porcentajes[indice])

        salida = f"{promedio:.2f}"

        actualizarSalida(salida)
        
    variables.datos.append(notas)
    variables.datos.append(porcentajes)
    variables.datos.append(promedio)

def widgetNuevo(contadorWidgets):
    
    nota = tk.StringVar(variables.listaWidgetsInicial[0])
    porcentaje = tk.StringVar(variables.listaWidgetsInicial[0])

    etiquetaNota = tk.Label(
        variables.listaWidgetsInicial[0],
        text=f"Nota {contadorWidgets}:",
        font=("Courier", 12, "bold"),
        justify="center",
        fg="white",
        bg="#00a8e8",
    )

    etiquetaNota.grid(
        padx=5,
        pady=5,
        row=0,
        column=variables.contadorWidgets + 3,
        sticky=tk.NSEW
    )

    etiquetaPorcentaje = tk.Label(
        variables.listaWidgetsInicial[0],
        text="Porcentaje(%):",
        font=("Courier", 12, "bold"),
        justify="center",
        fg="white",
        bg="#00a8e8",
    )

    etiquetaPorcentaje.grid(
        padx=5,
        pady=5,
        row=3,
        column=variables.contadorWidgets + 3,
        sticky=tk.NSEW
    )

    entradaNota = tk.Entry(
        variables.listaWidgetsInicial[0],
        justify="center",
        textvariable=nota
    )

    entradaNota.grid(
        padx=5,
        pady=5,
        row=1,
        column=variables.contadorWidgets + 3
        # sticky=tk.NSEW
    )

    entradaPorcentaje = tk.Entry(
        variables.listaWidgetsInicial[0],
        justify="center",
        textvariable=porcentaje
    )

    entradaPorcentaje.grid(
        padx=5,
        pady=5,
        row=5,
        column=variables.contadorWidgets + 3
        # sticky=tk.NSEW
    )

    entradaNota.insert(0, "Ingrese Nota")
    entradaPorcentaje.insert(0, "Ingrese Porcentaje")

    entradaNota.bind("<Double-1>", dobleClick1)
    entradaPorcentaje.bind("<Double-1>", dobleClick2)

    entradaNota.bind("<Return>", enter)
    entradaPorcentaje.bind("<Return>", enter)

    variables.listaWidgetsNuevos.append([etiquetaNota, entradaNota, etiquetaPorcentaje, entradaPorcentaje])
    variables.listaNotas.append(nota)
    variables.listaPorcentajes.append(porcentaje)

def agregarWidget():
    if variables.contadorWidgets == 6: return

    variables.contadorWidgets +=  1

    variables.listaWidgetsInicial[0].columnconfigure(variables.contadorWidgets + 3, minsize=50)
    variables.listaWidgetsInicial[0].columnconfigure(variables.contadorWidgets + 4, minsize=0)

    widgetNuevo(variables.contadorWidgets)

    variables.listaWidgetsInicial[3].grid(
        row=0,
        column=variables.contadorWidgets + 4,
        rowspan=6,
        sticky=tk.NSEW
    )

def eliminarWidget():
    if variables.contadorWidgets == 0: return

    variables.contadorWidgets -=  1

    variables.listaWidgetsInicial[0].columnconfigure(variables.contadorWidgets + 3, minsize=30)
    variables.listaWidgetsInicial[0].columnconfigure(variables.contadorWidgets + 4, minsize=0)

    for index in range(0, len(variables.listaWidgetsNuevos[0])):
        variables.listaWidgetsNuevos[-1][index].grid_forget()

    if variables.contadorWidgets >= 1:
        variables.listaWidgetsInicial[3].grid(
            row=0,
            column=variables.contadorWidgets + 4,
            rowspan=6,
            sticky=tk.NSEW
        )

    variables.listaWidgetsNuevos.pop()
    variables.listaNotas.pop()
    variables.listaPorcentajes.pop()

def actualizarSalida(texto):
    variables.listaWidgetsInicial[-1].configure(state=tk.NORMAL)
    variables.listaWidgetsInicial[-1].delete("0.0", tk.END)
    variables.listaWidgetsInicial[-1].insert("0.0", texto, "center")
    variables.listaWidgetsInicial[-1].configure(state="disabled")

def enter(event):
    calcularNota()

def dobleClick1(event):
    limpiarTextoNota()

def dobleClick2(event):
    limpiarTextoPorcentaje()

def reiniciar():
    for indice in range(0, len(variables.listaWidgetsNuevos)):
        eliminarWidget()
    
    actualizarSalida("Añadir Nota(s)")

def limpiarTextoNota():
    for index in range(0, len(variables.listaWidgetsNuevos)):
        variables.listaWidgetsNuevos[index][1].delete(0, tk.END)

def limpiarTextoPorcentaje():
    for index in range(0, len(variables.listaWidgetsNuevos)):
        variables.listaWidgetsNuevos[index][3].delete(0, tk.END)