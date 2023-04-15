from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("***JUEGA Y APRENDE***")

########### FUNCIONES ###################

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



def exit_program():
    root.destroy()
def clic_boton1():
    texto = Label(root, text="Bienvenido a Español").grid(row=1, column=3)
    boton6 = Button(root, text="APRENDAMOS", bg="ORANGE", width=10, height=3, command=clic_boton1).grid(row=1,column=5)
    boton7 = Button(root, text="JUGUEMOS", bg="ORANGE", width=10, height=3, command=clic_boton1).grid(row=1, column=7)

def clic_boton2():
    texto = Label(root, text="Bienvenido a Ciencias").grid(row=2, column=3)
    file = unicoArchivo("ciencias.txt")
    file = open('ciencias.txt', 'w')
    file.write('material de ciencias ')
    file.close()

def clic_boton3():
    texto = Label(root, text="Bienvenido a Mate").grid(row=3, column=3)

def clic_boton4():
        texto = Label(root, text="Bienvenido a Est. Sociales").grid(row=4, column=3)


############ CREACION DE LOS BOTONES PARA EL MENU #########
######## LLAMADO A LAS FUNCIONES #######

boton1 =Button(root,text="ESPAÑOL", bg="red",width=10,height=4, command=clic_boton1).grid(row=1, column=2)
boton2 =Button(root,text="CIENCIAS", bg="green",width=10,height=4, command=clic_boton2).grid(row=2, column=2)
boton3 =Button(root,text="MATE", bg="yellow",width=10,height=4, command=clic_boton3).grid(row=3, column=2)
boton4 =Button(root,text="EST. SOCIALES", bg="blue",width=10,height=4, command=clic_boton4).grid(row=4, column=2)
boton5 =Button(root,text="SALIR", bg="PURPLE",width=10,height=4, command=exit_program).grid(row=5, column=2)



# Configurar la ventana principal


root.mainloop()

