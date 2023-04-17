from tkinter import *
import tkinter as tk


########### CLASE SINGLETON ###################

class Singleton:
    _instance = None
    def __init__(self):
        print("Llamado al metodo Init")
        self.nombre = "Soy Unico"

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Llamado al metodo nueva instancia")
            cls._instance = object.__new__(cls)

        return cls._instance

    def getNombre(self):
        print("Llamdo a obtener atributo nombre")
        print(self.nombre)

    def setValor(self, valor):
        self.nombre = valor

class unicoArchivo():
    _instance = None
    file = None

    def __init__(self, NombreArchivo):
        self.matrix = [[1,2],[3,4],[5,6]]
        if self.file is None:
         self.file = open(NombreArchivo, 'w')

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Creando el unico archivo")
            cls._instance = object.__new__(cls)

        return cls._instance

    def agregar_a_matriz(self, linea):
        self.file.write(linea + '\n')

##########  CLASE VENTANA PRINCIPAL "#######
class VentanaPrincipal:
    def __init__(self, root):
        root.geometry("500x500")
        root.title("***JUEGA Y APRENDE***")
        self.root = root
        self.btn1 = Button(root, text="ESPAÑOL", bg="red",width=30,height=5, command=self.abrir_ventanaEspañol)
        self.btn1.pack()
        self.btn2 = Button(root, text="MATEMÁTICAS", bg="green",width=30,height=5, command=self.abrir_ventanaMatematicas)
        self.btn2.pack()
        self.btn3 = Button(root, text="CIENCIAS", bg="yellow", width=30, height=5, command=self.abrir_ventanaCiencias)
        self.btn3.pack()
        self.btn4 = Button(root, text="EST. SOCIALES", bg="blue", width=30, height=5, command=self.abrir_ventanaEspañol)
        self.btn4.pack()
        self.btn4 = Button(root, text="SALIR", bg="purple", width=20, height=4, command=self.exit_program)
        self.btn4.pack()

    def exit_program(self):
        root.destroy()
    def abrir_ventanaEspañol(self):
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="Contenido del archivo:")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="Leer archivo", command=self.leer_archivo)
        self.btn_leer.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="jugar", command=self.jugar)
        self.btn_leer.pack()


    def leer_archivo(self):
        with open("español.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)

    def jugar(self):
     entrada = Entry(root)
     entrada.pack()
     botonenviar = Button(self.ventana_secundaria, text="envias", command=self.clip)
     botonenviar.pack()
     texto = Label(root, text="se envio")
     texto.pack()
    def abrir_ventanaMatematicas(self):
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="Contenido del archivo:")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="Leer archivo", command=self.leer_archivoMate)
        self.btn_leer.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="jugar", command=self.jugar)
        self.btn_leer.pack()
    def leer_archivoMate(self):
        with open("mate.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)

    def abrir_ventanaCiencias(self):
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="**** MATERIAL CIENCIAS ****")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="Leer archivo", command=self.Archivo_Ciencias)
        self.btn_leer.pack()
        self.btn_leer1 = Button(self.ventana_secundaria, text="jugar", command=self.ventana_guardar)
        self.btn_leer1.pack()
         #nuevo
    def Archivo_Ciencias(self):
        with open("ciencias.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)
    def ventana_guardar(self):
        self.lbl = Label(self.ventana_secundaria, text="Ingrese la respuesta de cada pregunta, enumerandolas:")
        self.lbl.pack()
        self.entrada = Entry(self.ventana_secundaria)
        self.entrada.pack()
        self.btn_guardar = Button(self.ventana_secundaria, text="Guardar", command=self.guardar_archivo)
        self.btn_guardar.pack()
        self.btn_leerpreguntas = Button(self.ventana_secundaria, text="leer", command=self.guardar_archivo)
        self.btn_leerpreguntas.pack()
# # guardar
    def guardar_archivo(self):
         contenido = self.entrada.get()
         with open("preguntasciencias.txt", "a") as f:
            f.write(contenido + "\n")
         self.entrada.delete(0, tk.END)
         self.leer_archivo()

         with open("preguntasciencias.txt", "r") as f:
            contenido = f.read()
         self.texto.delete("1.0", tk.END)
         self.texto.insert(tk.END, contenido)


# # #Configurar la ventana principal
root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()

