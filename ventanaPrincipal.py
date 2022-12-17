import tkinter as tk
from tkinter import ttk

import funciones
import variables


## ==============================================
## Ventana Principal
## ==============================================

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("TuNota!")
# ventanaPrincipal.minsize(330, 200)
ventanaPrincipal.resizable(0, 0)
ventanaPrincipal.configure(background="#B2FFFF")

ventanaPrincipal.columnconfigure(0, minsize=150)
ventanaPrincipal.columnconfigure(1, minsize=150)
ventanaPrincipal.columnconfigure(2, minsize=0)
ventanaPrincipal.columnconfigure(3, minsize=30)

ventanaPrincipal.rowconfigure(0, minsize=50)
ventanaPrincipal.rowconfigure(1, minsize=50)
ventanaPrincipal.rowconfigure(2, minsize=0)
ventanaPrincipal.rowconfigure(3, minsize=50)
ventanaPrincipal.rowconfigure(4, minsize=0)
ventanaPrincipal.rowconfigure(5, minsize=50)

## ==============================================
## Widgets
## ==============================================

# ================
# Pantalla Inicial
# ================

etiquetaInicial = tk.Label(
    ventanaPrincipal,
    text="TuNota!",
    font=("Courier", 19),
    justify="center",
    # fg="white",
    bg="#B2FFFF",
)

etiquetaInicial.grid(
    # padx=1,
    # pady=1,
    row=0,
    column=0,
    rowspan=2,
    columnspan=2,
    sticky=tk.NSEW
)

# salidaPromedio = tk.Entry(
#     ventanaPrincipal,
#     justify="center",
#     bd=3,
#     fg="red",
#     selectbackground="red",
#     # selectborderwidth=10,
#     # relief=tk.RIDGE
#     # font=("Courier", 8, "bold")
# )

salidaPromedio = tk.Text(
    ventanaPrincipal,
    # justify="center",
    bd=3,
    fg="red",
    selectbackground="red",
    width=12,
    height=2,
    padx=6,
    pady=6,
    wrap=tk.WORD,
    # font=("Courier", 8, "bold")
)

salidaPromedio.grid(
    row=3,
    column=1,
)

botonCalcular = tk.Button(
    ventanaPrincipal,
    text="Calcular",
    fg="white",
    bg="blue",
    justify="center",
    height = 2, 
    width = 15,
    command=funciones.calcularNota
)

botonCalcular.grid(
    padx=5,
    pady=5,
    row=3,
    column=0,
    # sticky=tk.NSEW
)

# ================
# Separadores
# ================

separadorHorizontal1 = ttk.Separator(
    ventanaPrincipal,
    orient="horizontal",
)

separadorHorizontal1.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky=tk.EW
)

separadorHorizontal2 = ttk.Separator(
    ventanaPrincipal,
    orient="horizontal",
)

separadorHorizontal2.grid(
    row=4,
    column=0,
    columnspan=2,
    sticky=tk.EW
)

separadorVertical2 = ttk.Separator(
    ventanaPrincipal,
    orient="vertical",
)

separadorVertical2.grid(
    row=0,
    column=2,
    rowspan=6,
    sticky=tk.NSEW
)

separadorVertical3 = ttk.Separator(
    ventanaPrincipal,
    orient="vertical",
)

# ================
# Botones
# ================

botonGuardar = tk.Button(
    ventanaPrincipal,
    text="Guardar",
    fg="white",
    bg="red",
    justify="center",
    # height = 2, 
    # width = 15
    # font=("Courier", 16)
    # command=agregarWidget
)

botonGuardar.grid(
    padx=5,
    pady=5,
    row=5,
    column=0,
    sticky=tk.NSEW
)

botonReiniciar = tk.Button(
    ventanaPrincipal,
    text="Reiniciar",
    fg="white",
    bg="red",
    justify="center",
    # height = 2, 
    # width = 15
    # font=("Courier", 16)
    command=funciones.reiniciar
)

botonReiniciar.grid(
    padx=5,
    pady=5,
    row=5,
    column=1,
    sticky=tk.NSEW
)

# ==========================
# Pestaña Agregar y Eliminar
# ==========================

botonAñadir = tk.Button(
    ventanaPrincipal,
    text="+",
    fg="white",
    bg="green",
    justify="center",
    width=2,
    height=6,
    command=funciones.agregarWidget
)

botonAñadir.grid(
    row=0,
    column=3,
    rowspan=3,
    # sticky=tk.NS
)

botonEliminar = tk.Button(
    ventanaPrincipal,
    text="-",
    fg="white",
    bg="green",
    justify="center",
    width=2,
    height=6,
    command=funciones.eliminarWidget
)

botonEliminar.grid(
    row=3,
    column=3,
    rowspan=3,
    # sticky=tk.NS
)

variables.listaWidgetsInicial.append(ventanaPrincipal)
variables.listaWidgetsInicial.append(botonAñadir)
variables.listaWidgetsInicial.append(botonEliminar)
variables.listaWidgetsInicial.append(separadorVertical3)
variables.listaWidgetsInicial.append(salidaPromedio)

salidaPromedio.tag_configure("center", justify='center')
salidaPromedio.tag_add("center", "0.0", "end")
funciones.actualizarSalida("Añadir Notas")

ventanaPrincipal.mainloop()