def saludar():
    print('Hola')


from tkinter import*
ventana=Tk()
boton=Button(ventana, text='Púlsame', command=saludar)
boton.pack()



