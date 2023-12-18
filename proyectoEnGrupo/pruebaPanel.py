import tkinter as tk
from PIL import Image, ImageTk


def accion_boton(numero):
    print(f"Botón {numero} presionado")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("IPC2 MUSIC")
ventana.geometry(f"{970}x{636}+{100}+{50}")
ventana.config(bg="black")

altoPanel = ventana.winfo_screenheight()
anchoPanel = ventana.winfo_screenwidth()
anchoPanel = anchoPanel - 583
# Crear el panel
panel = tk.Frame(ventana, bg="#0c131a", width="250", height=altoPanel)
panel.place(x=0, y=70)

panelTitulo = tk.Frame(ventana, bg="#0c131a", width=anchoPanel, height="50")
panelTitulo.place(x=7, y=10)

labeltitulo = tk.Label(panelTitulo, text="IPC2 MUSIC", font=("", "26"), fg="blue", background="black")
labeltitulo.place(x="400", y="0")

# Crear varios botones dentro del panel
boton = tk.Button(panel, text="PlayListalgo ", font=("", "16"), command=lambda num="playlist": accion_boton(num),
                  bg="#0c131a", fg="white", width="20", height="1")
# boton = tk.Button(panel, text="PlayListalgo", font=("", "16"), command=lambda num="playlist": accion_boton(num))
boton.place(x="0", y="0")

boton = tk.Button(panel, text="Biblioteca ", command=lambda num="playlist": accion_boton(num), font=("", "16"),
                  width="20", height="1", bg="#0c131a", fg="white")
# boton = tk.Button(panel, text="Biblioteca ", font=("", "16"), command=lambda num="playlist": accion_boton(num), width="20", height="1", bg="#0d0e0f", fg="white")
# boton = tk.Button(panel, text="PlayListalgo", font=("", "16"), command=lambda num="playlist": accion_boton(num))
boton.place(x="0", y="42")

# Iniciar el bucle principal de la aplicación


colorPanel = "#041424"


def crear_bordes_redondeados(canvas, x, y, width, height, radio):
    # Crear bordes redondeados
    canvas.create_arc(x, y, x + 2 * radio, y + 2 * radio, start=90, extent=90, fill=colorPanel, outline=colorPanel)
    canvas.create_arc(x + width - 2 * radio, y, x + width, y + 2 * radio, start=0, extent=90, fill=colorPanel,
                      outline=colorPanel)
    canvas.create_arc(x, y + height - 2 * radio, x + 2 * radio, y + height, start=180, extent=90, fill=colorPanel,
                      outline=colorPanel)
    canvas.create_arc(x + width - 2 * radio, y + height - 2 * radio, x + width, y + height, start=270, extent=90,
                      fill=colorPanel, outline=colorPanel)

    # Crear segmentos rectos
    canvas.create_rectangle(x + radio, y, x + width - radio, y + height, fill=colorPanel, outline=colorPanel)
    canvas.create_rectangle(x, y + radio, x + width, y + height - radio, fill=colorPanel, outline=colorPanel)

    # Configurar las dimensiones del panel


ancho_panel = 700
alto_panel = 500
radio_bordes = 5

# Crear el Canvas para el panel
panelImagenArtista = tk.Canvas(ventana, width=ancho_panel, height=alto_panel, bg="black", highlightthickness=0)
panelImagenArtista.place(x="260", y="70")
# panelImagenArtista.config(bg="black")
panelReproduccion = tk.Canvas(ventana, width=ancho_panel, height=50, bg="black", highlightthickness=0)
panelReproduccion.place(x="260", y="580")

# Crear bordes redondeados en el Canvas
crear_bordes_redondeados(panelImagenArtista, 0, 0, ancho_panel, alto_panel, radio_bordes)
crear_bordes_redondeados(panelReproduccion, 0, 0, ancho_panel, alto_panel, radio_bordes)


# # Crear un botón dentro del panel
# boton_panel = tk.Button(canvas_panel, text="Presionar", command=accion_boton)
# boton_panel.place(x="300", y="100")

# Agregando boton de Play en el panel


def accion_boton():
    print("Botón presionado")


# Crear la ventana principal

# Cargar la imagen
# ruta_imagen = "buttonPlay.png"  # Cambiar la ruta a tu imagen
# imagen = Image.open(ruta_imagen)
# imagen = imagen.resize((40, 40), Image.LANCZOS)  # Ajusta el tamaño de la imagen
# imagen_botonPlay = ImageTk.PhotoImage(imagen)

# ruta_imagen = "adelantarCancion.png"  # Cambiar la ruta a tu imagen
# imagen = Image.open(ruta_imagen)
# imagen = imagen.resize((40, 40), Image.LANCZOS)  # Ajusta el tamaño de la imagen
# imagen_botonAdelantar = ImageTk.PhotoImage(imagen)

# ruta_imagen = "regresarCancion.png"  # Cambiar la ruta a tu imagen
# imagen = Image.open(ruta_imagen)
# imagen = imagen.resize((40, 40), Image.LANCZOS)  # Ajusta el tamaño de la imagen
# imagen_botonRegresar = ImageTk.PhotoImage(imagen)

# Crear el botón con la imagen
# boton_play = tk.Button(panelImagenArtista, image=imagen_botonPlay, command=accion_boton, bg="#292c30")
# boton_play.place(x="320", y="450")

# boton_regresar = tk.Button(panelImagenArtista, image=imagen_botonRegresar, command=accion_boton, bg="#292c30")
# boton_regresar.place(x="274", y="450")

# boton_adelantar = tk.Button(panelImagenArtista, image=imagen_botonAdelantar, command=accion_boton, bg="#292c30")
# boton_adelantar.place(x="365", y="450")

# print("ancho panel: ", anchoPanel)
ventana.mainloop()