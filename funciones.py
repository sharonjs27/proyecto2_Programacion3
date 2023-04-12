from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("***JUEGA Y APRENDE***")

########### FUNCIONES ###################
def exit_program():
    root.destroy()
def clic_boton1():
    texto = Label(root, text="no lo vuelvas a precionar").grid(row=1, column=3)
def clic_boton2():
    texto = Label(root, text="hola").grid(row=2, column=3)
def clic_boton3():
    texto = Label(root, text="adios").grid(row=3, column=3)

def clic_boton4():
        texto = Label(root, text="buenas").grid(row=4, column=3)


############ CREACION DE LOS BOTONES PARA EL MENU #########
######## LLAMADO A LAS FUNCIONES #######

boton1 =Button(root,text="ESPAÑOL", bg="red",width=10,height=4, command=clic_boton1).grid(row=1, column=2)
boton2 =Button(root,text="CIENCIAS", bg="green",width=10,height=4, command=clic_boton2).grid(row=2, column=2)
boton3 =Button(root,text="MATE", bg="yellow",width=10,height=4, command=clic_boton3).grid(row=3, column=2)
boton4 =Button(root,text="EST. SOCIALES", bg="blue",width=10,height=4, command=clic_boton4).grid(row=4, column=2)
boton5 =Button(root,text="SALIR", bg="PURPLE",width=10,height=4, command=exit_program).grid(row=5, column=2)



# Configurar la ventana principal
root.mainloop()

