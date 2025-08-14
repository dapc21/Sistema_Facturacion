from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

# Paleta de colores moderna y comercial
COLOR_PRIMARY = '#2C3E50'      # Azul marino oscuro - Profesional
COLOR_SECONDARY = '#3498DB'    # Azul brillante - Confianza
COLOR_ACCENT = '#E74C3C'       # Rojo coral - Acción
COLOR_SUCCESS = '#27AE60'      # Verde esmeralda - Éxito
COLOR_WARNING = '#F39C12'      # Naranja dorado - Atención
COLOR_LIGHT = '#ECF0F1'        # Gris muy claro - Fondo
COLOR_WHITE = '#FFFFFF'        # Blanco puro
COLOR_DARK_TEXT = '#2C3E50'    # Texto oscuro
COLOR_LIGHT_TEXT = '#FFFFFF'   # Texto claro
COLOR_HOVER = '#34495E'        # Azul gris para hover


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1300x750+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# título de la ventana
aplicacion.title("Restaurante DP - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg=COLOR_LIGHT)

# panel superior
panel_superior = Frame(aplicacion, bd=2, relief=RAISED, bg=COLOR_PRIMARY)
panel_superior.pack(side=TOP, fill=X)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior,
                        text='🍽️ SISTEMA DE FACTURACIÓN 🍽️',
                        fg=COLOR_LIGHT_TEXT,
                        font=('Arial', 28, 'bold'),
                        bg=COLOR_PRIMARY,
                        width=40,
                        pady=15)
etiqueta_titulo.pack(expand=True)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT, bg=COLOR_LIGHT)
panel_izquierdo.pack(side=LEFT, padx=5, pady=5)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=3, relief=RAISED, bg=COLOR_WHITE, padx=15, pady=10)
panel_costos.pack(side=BOTTOM, pady=(5, 0))

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo,
                          text='🥘 COMIDAS',
                          font=('Arial', 16, 'bold'),
                          bd=3,
                          relief=RAISED,
                          fg=COLOR_DARK_TEXT,
                          bg=COLOR_WHITE,
                          padx=10,
                          pady=10)
panel_comidas.pack(side=LEFT, padx=(0, 5))

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                          text='🥤 BEBIDAS',
                          font=('Arial', 16, 'bold'),
                          bd=3,
                          relief=RAISED,
                          fg=COLOR_DARK_TEXT,
                          bg=COLOR_WHITE,
                          padx=10,
                          pady=10)
panel_bebidas.pack(side=LEFT, padx=5)

# panel postres
panel_postres = LabelFrame(panel_izquierdo,
                          text='🍰 POSTRES',
                          font=('Arial', 16, 'bold'),
                          bd=3,
                          relief=RAISED,
                          fg=COLOR_DARK_TEXT,
                          bg=COLOR_WHITE,
                          padx=10,
                          pady=10)
panel_postres.pack(side=LEFT, padx=(5, 0))

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT, bg=COLOR_LIGHT)
panel_derecha.pack(side=RIGHT, padx=0, pady=5)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=3, relief=RAISED, bg=COLOR_WHITE, padx=0, pady=8)
panel_calculadora.pack(pady=(0, 5))

# panel recibo
panel_recibo = Frame(panel_derecha, bd=3, relief=RAISED, bg=COLOR_WHITE, padx=0, pady=8)
panel_recibo.pack(pady=3)

# panel botones
panel_botones = Frame(panel_derecha, bd=3, relief=RAISED, bg=COLOR_WHITE, padx=0, pady=8)
panel_botones.pack(pady=(0, 35))

# lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmón', 'Merluza', 'Kebab', 'Pizza Margarita', 'Pizza Pepperoni', 'Pizza Suprema']
lista_bebidas = ['Agua', 'Soda', 'Jugo Natural', 'Cola', 'Vino Tinto', 'Vino Blanco', 'Cerveza Nacional', 'Cerveza Importada']
lista_postres = ['Helado', 'Fruta Fresca', 'Brownies', 'Flan', 'Mousse', 'Pastel Chocolate', 'Pastel Vainilla', 'Pastel Fresa']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida_check = Checkbutton(panel_comidas,
                         text=comida,
                         font=('Arial', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check,
                         bg=COLOR_WHITE,
                         fg=COLOR_DARK_TEXT,
                         selectcolor=COLOR_SUCCESS,
                         activebackground=COLOR_LIGHT,
                         activeforeground=COLOR_DARK_TEXT)

    comida_check.grid(row=contador,
                column=0,
                sticky=W,
                pady=2)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Arial', 11, 'bold'),
                                     bd=2,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador],
                                     justify=CENTER,
                                     bg=COLOR_LIGHT,
                                     fg=COLOR_DARK_TEXT,
                                     insertbackground=COLOR_SECONDARY)
    cuadros_comida[contador].grid(row=contador,
                                  column=1,
                                  padx=(10, 0),
                                  pady=2)
    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida_check = Checkbutton(panel_bebidas,
                         text=bebida,
                         font=('Arial', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check,
                         bg=COLOR_WHITE,
                         fg=COLOR_DARK_TEXT,
                         selectcolor=COLOR_SUCCESS,
                         activebackground=COLOR_LIGHT,
                         activeforeground=COLOR_DARK_TEXT)
    bebida_check.grid(row=contador,
                column=0,
                sticky=W,
                pady=2)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Arial', 11, 'bold'),
                                     bd=2,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador],
                                     justify=CENTER,
                                     bg=COLOR_LIGHT,
                                     fg=COLOR_DARK_TEXT,
                                     insertbackground=COLOR_SECONDARY)
    cuadros_bebida[contador].grid(row=contador,
                                  column=1,
                                  padx=(10, 0),
                                  pady=2)

    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    # crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres_check = Checkbutton(panel_postres,
                          text=postres,
                          font=('Arial', 12, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                         command=revisar_check,
                         bg=COLOR_WHITE,
                         fg=COLOR_DARK_TEXT,
                         selectcolor=COLOR_SUCCESS,
                         activebackground=COLOR_LIGHT,
                         activeforeground=COLOR_DARK_TEXT)
    postres_check.grid(row=contador,
                 column=0,
                 sticky=W,
                 pady=2)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Arial', 11, 'bold'),
                                      bd=2,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador],
                                      justify=CENTER,
                                      bg=COLOR_LIGHT,
                                      fg=COLOR_DARK_TEXT,
                                      insertbackground=COLOR_SECONDARY)
    cuadros_postres[contador].grid(row=contador,
                                   column=1,
                                   padx=(10, 0),
                                   pady=2)
    contador += 1


# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Arial', 11, 'bold'),
                              bg=COLOR_WHITE,
                              fg=COLOR_DARK_TEXT)
etiqueta_costo_comida.grid(row=0, column=0, sticky=W, pady=3)

texto_costo_comida = Entry(panel_costos,
                           font=('Arial', 11, 'bold'),
                           bd=2,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_comida,
                           justify=CENTER,
                           bg=COLOR_LIGHT,
                           fg=COLOR_DARK_TEXT)
texto_costo_comida.grid(row=0, column=1, padx=20, pady=3)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Arial', 11, 'bold'),
                              bg=COLOR_WHITE,
                              fg=COLOR_DARK_TEXT)
etiqueta_costo_bebida.grid(row=1, column=0, sticky=W, pady=3)

texto_costo_bebida = Entry(panel_costos,
                           font=('Arial', 11, 'bold'),
                           bd=2,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_bebida,
                           justify=CENTER,
                           bg=COLOR_LIGHT,
                           fg=COLOR_DARK_TEXT)
texto_costo_bebida.grid(row=1, column=1, padx=20, pady=3)

etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Arial', 11, 'bold'),
                              bg=COLOR_WHITE,
                              fg=COLOR_DARK_TEXT)
etiqueta_costo_postres.grid(row=2, column=0, sticky=W, pady=3)

texto_costo_postres = Entry(panel_costos,
                           font=('Arial', 11, 'bold'),
                           bd=2,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_postres,
                           justify=CENTER,
                           bg=COLOR_LIGHT,
                           fg=COLOR_DARK_TEXT)
texto_costo_postres.grid(row=2, column=1, padx=20, pady=3)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Arial', 11, 'bold'),
                              bg=COLOR_WHITE,
                              fg=COLOR_DARK_TEXT)
etiqueta_subtotal.grid(row=0, column=2, sticky=W, pady=3)

texto_subtotal = Entry(panel_costos,
                           font=('Arial', 11, 'bold'),
                           bd=2,
                           width=12,
                           state='readonly',
                           textvariable=var_subtotal,
                           justify=CENTER,
                           bg=COLOR_LIGHT,
                           fg=COLOR_DARK_TEXT)
texto_subtotal.grid(row=0, column=3, padx=20, pady=3)

etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Arial', 11, 'bold'),
                              bg=COLOR_WHITE,
                              fg=COLOR_DARK_TEXT)
etiqueta_impuestos.grid(row=1, column=2, sticky=W, pady=3)

texto_impuestos = Entry(panel_costos,
                           font=('Arial', 11, 'bold'),
                           bd=2,
                           width=12,
                           state='readonly',
                           textvariable=var_impuestos,
                           justify=CENTER,
                           bg=COLOR_LIGHT,
                           fg=COLOR_DARK_TEXT)
texto_impuestos.grid(row=1, column=3, padx=20, pady=3)

etiqueta_total = Label(panel_costos,
                              text='💰 TOTAL',
                              font=('Arial', 12, 'bold'),
                              bg=COLOR_WHITE,
                              fg=COLOR_SUCCESS)
etiqueta_total.grid(row=2, column=2, sticky=W, pady=3)

texto_total = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=3,
                           width=12,
                           state='readonly',
                           textvariable=var_total,
                           justify=CENTER,
                           bg=COLOR_SUCCESS,
                           fg=COLOR_WHITE)
texto_total.grid(row=2, column=3, padx=20, pady=3)

# botones principales
botones_info = [
    ('💵 Total', COLOR_SECONDARY),
    ('📋 Recibo', COLOR_WARNING),
    ('💾 Guardar', COLOR_SUCCESS),
    ('🔄 Resetear', COLOR_ACCENT)
]
botones_creados = []

columnas = 0
for texto_boton, color in botones_info:
    boton = Button(panel_botones,
                   text=texto_boton,
                   font=('Arial', 11, 'bold'),
                   fg=COLOR_WHITE,
                   bg=color,
                   bd=2,
                   width=10,
                   height=1,
                   relief=RAISED,
                   cursor='hand2')

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas,
               padx=3,
               pady=3)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
Label(panel_recibo,
      text='📄 RECIBO DE COMPRA',
      font=('Arial', 14, 'bold'),
      bg=COLOR_WHITE,
      fg=COLOR_DARK_TEXT).grid(row=0, column=0, pady=(0, 10))

texto_recibo = Text(panel_recibo,
                    font=('Courier New', 9, 'bold'),
                    bd=2,
                    width=45,
                    height=10,
                    bg=COLOR_LIGHT,
                    fg=COLOR_DARK_TEXT,
                    insertbackground=COLOR_SECONDARY)
texto_recibo.grid(row=1, column=0)

# calculadora
Label(panel_calculadora,
      text='🧮 CALCULADORA',
      font=('Arial', 14, 'bold'),
      bg=COLOR_WHITE,
      fg=COLOR_DARK_TEXT).grid(row=0, column=0, columnspan=4, pady=(0, 10))

visor_calculadora = Entry(panel_calculadora,
                          font=('Arial', 12, 'bold'),
                          width=25,
                          bd=3,
                          justify=RIGHT,
                          bg=COLOR_LIGHT,
                          fg=COLOR_DARK_TEXT,
                          insertbackground=COLOR_SECONDARY)
visor_calculadora.grid(row=1,
                       column=0,
                       columnspan=4,
                       pady=(0, 10))

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', '×', '=', 'C', '0', '÷']
colores_calc = [COLOR_PRIMARY, COLOR_PRIMARY, COLOR_PRIMARY, COLOR_SECONDARY,
                COLOR_PRIMARY, COLOR_PRIMARY, COLOR_PRIMARY, COLOR_SECONDARY,
                COLOR_PRIMARY, COLOR_PRIMARY, COLOR_PRIMARY, COLOR_SECONDARY,
                COLOR_SUCCESS, COLOR_ACCENT, COLOR_PRIMARY, COLOR_SECONDARY]

botones_guardados = []

fila = 2
columna = 0
for i, boton in enumerate(botones_calculadora):
    boton_calc = Button(panel_calculadora,
                   text=boton,
                   font=('Arial', 12, 'bold'),
                   fg=COLOR_WHITE,
                   bg=colores_calc[i],
                   bd=2,
                   width=6,
                   height=2,
                   cursor='hand2')

    botones_guardados.append(boton_calc)

    boton_calc.grid(row=fila,
               column=columna,
               padx=2,
               pady=2)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

# Configurar comandos de calculadora
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# evitar que la pantalla se cierre
aplicacion.mainloop()