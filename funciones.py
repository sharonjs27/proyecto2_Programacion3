from tkinter import *
import tkinter as tk


########### CLASE SINGLETON ###################


class UnicoArchivo():
    _instance = None
    file = None
    def __init__(self, NombreArchivo):
        if self.file is None:
         self.file = open(NombreArchivo, 'w')

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Creando el unico archivo")
            cls._instance = object.__new__(cls)

        return cls._instance

##########  CLASE VENTANA PRINCIPAL "#######
class VentanaPrincipal:
    def __init__(self, root):
        root.geometry("500x500")
        root.title("*** JUEGA Y APRENDE ***")
        self.root = root
        self.btn1 = Button(root, text="  ESPAÑOL  ", bg="red", width=30, height=5, command=self.AbrirVentanaEspañol)
        self.btn1.pack()
        self.btn2 = Button(root, text="  MATEMÁTICAS  ", bg="green", width=30, height=5, command=self.AbrirVentanaMatematicas)
        self.btn2.pack()
        self.btn3 = Button(root, text="  CIENCIAS  ", bg="yellow", width=30, height=5, command=self.AbrirVentanaCiencias)
        self.btn3.pack()
        self.btn4 = Button(root, text="  EXPERIENCIA  ", bg="blue", width=30, height=5, command=self.AbrirVentanaExperiencia)
        self.btn4.pack()
        self.btn4 = Button(root, text="  buscar material ", bg="pink", width=30, height=5, command=self.AbrirArchivosExisten)
        self.btn4.pack()
        self.btn5 = Button(root, text="SALIR", bg="purple", width=20, height=4, command=self.SalirPrograma)
        self.btn5.pack()

    def SalirPrograma(self):
        root.destroy()



    ########################  OPCION ESPAÑOL #########################################
    def AbrirVentanaEspañol(self):                       ##  Ventana principal de español para leer y jugar
        self.ventana_secundaria = Toplevel(self.root)    ## se abre una segunda ventana
        self.lbl = Label(self.ventana_secundaria, text="****** Bienvenido a Español *******")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="Leer Material", command=self.LeerArchivo)
        self.btn_leer.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="jugar", command=self.JugarEspañol)
        self.btn_leer.pack()
        self.btn_Silabas = Button(self.ventana_secundaria, text="division de palabas en silabas",
                                        command=self.Silabas)
        self.btn_Silabas.pack()
    def LeerArchivo(self):                    ## funcion para leer el archivo de español donde se encuentra la materia
        with open("español.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)

    def JugarEspañol(self):              ## ventana para realizar la redaccion
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="REDACCION")
        self.lbl.pack()
        self.lbl = Label(self.ventana_secundaria,
                         text="ESCRIBA UNA REDACCION DE UN PARRAFO CON LAS PALABRAS ARBOL, NUBES, AGUA : ")
        self.lbl.pack()
        self.entrada = Entry(self.ventana_secundaria)
        self.entrada.pack()
        self.btn_guardarRedaccion = Button(self.ventana_secundaria, text="GUARDAR",
                                           command=self.GuardarArchivoRedaccion)
        self.btn_guardarRedaccion.pack()

    def GuardarArchivoRedaccion(self):
        redaccion = self.entrada.get()              ## guarda lo escrito en el archivo creado para la redacción
        file = UnicoArchivo("redaccion.txt")
        with open("redaccion.txt", "a") as f:
            f.write(redaccion + "\n")
        self.entrada.delete(0, tk.END)

        with open("redaccion.txt", "r") as f:          ## Leer el archivo redactado
          contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)
    def Silabas(self):
        self.ventana_secundaria = Toplevel(self.root)
        matriz = []
        for i in range(3):
            self.fila = []
            for j in range(3):
                self.entrada = Entry(self.ventana_secundaria, width=5)
                self.entrada.grid(row=i, column=j)
                self.fila.append(self.entrada)
            matriz.append(self.fila)

        #################### OPCION MATEMATICAS ###################################
    def AbrirVentanaMatematicas(self):    ## Ventana principal de matemáticas, muestras
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="***** MATERIAL MATEMÁTICAS *****")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text=" LEER MATERIA ", command=self.ArchivoMate)
        self.btn_leer.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="JUGAR", command=self.JugarMate)
        self.btn_leer.pack()

    def ArchivoMate(self):     ## se lee el archivo preparado con la materia
        with open("mate.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)
    def JugarMate(self):
         self.ventana_secundaria = Toplevel(self.root)    ## ventana que pide seguir la secuencia del mensaje mostrado
         self.lbl = Label(self.ventana_secundaria, text="**** SECUENCIAS ****")
         self.lbl.pack()
         self.lbl = Label(self.ventana_secundaria, text="escribe la secuencia de numeros : ")
         self.lbl.pack()
         self.entrada = Entry(self.ventana_secundaria)
         self.entrada.pack()
         self.btn_guardarSecuencia = Button(self.ventana_secundaria, text="GUARDAR",
                                            command=self.GuardarArchivoSecuencias)
         self.btn_guardarSecuencia.pack()

         self.secuencias1 = ("5", "10", "15", "20", ".....")        ## secuencia mostrada en la ventana
         self.texto.delete("1.0", tk.END)
         self.texto.insert(tk.END, self.secuencias1)

    def GuardarArchivoSecuencias(self):      ## guarda un unico archivo con las secuencia realizada en la ventada anterior
        contenido = self.entrada.get()
        file = UnicoArchivo("secuencias.txt")
        with open("secuencias.txt", "a") as f:
            f.write(contenido + "\n")
        self.entrada.delete(0, tk.END)

        with open("secuencias.txt", "r") as f:   ## muestra el archivo que se guardo y modificó
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)



    ################# opcion ciencias ################################################################
    def AbrirVentanaCiencias(self):   ## Ventana principal de ciencias
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="**** MATERIAL CIENCIAS ****")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text=" LEER MATERIA ", command=self.ArchivoCiencias)
        self.btn_leer.pack()
        self.btn_leer1 = Button(self.ventana_secundaria, text=" JUGAR ", command=self.VentanaGuardar)
        self.btn_leer1.pack()
    def ArchivoCiencias(self):         ## se lee el archivo creado con anticipación con el material
        with open("ciencias.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)
    def VentanaGuardar(self):    ## se introduce las respuestas de las preguntas
        self.lbl = Label(self.ventana_secundaria, text="Ingrese la respuesta de cada pregunta, enumerandolas:")
        self.lbl.pack()
        self.entrada = Entry(self.ventana_secundaria)
        self.entrada.pack()
        self.btn_guardar = Button(self.ventana_secundaria, text="GUARDAR", command=self.GuardarArchivo)
        self.btn_guardar.pack()
        self.btn_leerpreguntas = Button(self.ventana_secundaria, text="PREGUNTAS", command=self.GuardarArchivo)
        self.btn_leerpreguntas.pack()
    def GuardarArchivo(self):        ## se guardan las rspustas en el mismo archivo de las preguntas
         contenido = self.entrada.get()

         with open("preguntasciencias.txt", "a") as f:
            f.write(contenido + "\n")
         self.entrada.delete(0, tk.END)


         with open("preguntasciencias.txt", "r") as f: ## se lee el archivo de las preguntas
            contenido = f.read()
         self.texto.delete("1.0", tk.END)
         self.texto.insert(tk.END, contenido)

   ######################### opcion expeciencia ###################
    def AbrirVentanaExperiencia(self):
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="**** EXPERIENCIA ****")
        self.lbl.pack()
        self.texto = Text(self.ventana_secundaria)
        self.texto.pack()
        self.btn_leer = Button(self.ventana_secundaria, text="LEER MENSAJE", command=self.ArchivoExperiencia)
        self.btn_leer.pack()
        self.btn_leer1 = Button(self.ventana_secundaria, text="GUARDAR RESPUESTA",
                                command=self.VentanaGuardarExperiencia)
        self.btn_leer1.pack()
    def ArchivoExperiencia(self):      ### muestra mensaje para solicitar al usuario dar opinion sobre la programa
        with open("experiencia.txt", "r") as f:
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)

    def VentanaGuardarExperiencia(self):   ## se guarda la experiencia
        self.lbl = Label(self.ventana_secundaria, text="Relate su experiencia: ")
        self.lbl.pack()
        self.entrada = Entry(self.ventana_secundaria)
        self.entrada.pack()
        self.btn_guardar = Button(self.ventana_secundaria, text="Guardar", command=self.GuardarArchivoExperiencia)
        self.btn_guardar.pack()
        self.btn_leerpreguntas = Button(self.ventana_secundaria, text="leer", command=self.GuardarArchivoExperiencia)
        self.btn_leerpreguntas.pack()

    def GuardarArchivoExperiencia(self):  ## se crea un unico archivo con la experiencia
        contenido = self.entrada.get()
        file = UnicoArchivo("experienciaGanada.txt")
        with open("experienciaGanada.txt", "a") as f:
            f.write(contenido + "\n")
        self.entrada.delete(0, tk.END)
        with open("experienciaGanada.txt", "r") as f:      ## se lee el archivo creado
            contenido = f.read()
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, contenido)
 ##########################  buscar material    ##################################
    def AbrirArchivosExisten(self):    ## se solicita escribir el archivo que se busca
        self.ventana_secundaria = Toplevel(self.root)
        self.lbl = Label(self.ventana_secundaria, text="Ingrese el Archivo a Buscar:")
        self.lbl.pack()
        self.nombreBuscado = Entry(self.ventana_secundaria)
        self.nombreBuscado.pack()
        self.btn_buscar = Button(self.ventana_secundaria, text="BUSCAR", command=self.ArchivoBuscado)
        self.btn_buscar.pack()

    def ArchivoBuscado(self): ## funcion de excepcion si el archivo no exite muestra un mensaje y si existe se lee
        try:
           f=open(self.nombreBuscado, "r")
           f.close()
           return True
        except:
           print("no existe")
           self.lbl = Label(self.ventana_secundaria, text=" NO EXISTE ")
           self.lbl.pack()
        else:
            with open( "nombreBuscado", "r") as f:
                contenido = f.read()
            self.texto.delete("1.0", tk.END)
            self.texto.insert(tk.END, contenido)

root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()

