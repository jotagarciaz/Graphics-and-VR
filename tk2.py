import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.ventana1, width=1000, height=800, background="black")
        self.canvas1.grid(column=0, row=0)

        points = [[118, 345],[118, 138],[436, 345],[436,138],[268,75],[218,345],[298,345],[298,240],[218,240]]
        self.canvas1.create_line(points[0],points[1] ,fill="gold")
        self.canvas1.create_line(points[0], points[2] ,fill="gold")
        self.canvas1.create_line(points[2] , points[3],fill="gold")
        self.canvas1.create_line(points[1],  points[3],fill="gold")
        self.canvas1.create_line(points[1], points[4],fill="gold")
        self.canvas1.create_line(points[4],  points[3],fill="gold")
        #puerta
        self.canvas1.create_line(points[5],  points[8],fill="gold")
        self.canvas1.create_line(points[6],  points[7],fill="gold")
        self.canvas1.create_line(points[7],  points[8],fill="gold")

        self.ventana1.mainloop()

        

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.ventana1,text="Transformaciones 2D")
        self.lf1.grid(column=1, row=0, sticky="w")
       
        # Transladar #
        self.label1=ttk.Label(self.lf1, text="Transladar")
        self.label1.grid(column=0,row=0, padx=5, pady=5)

        self.label1=ttk.Label(self.lf1, text="x")
        self.label1.grid(column=0,row=1, padx=1, pady=1)

        self.dato1=tk.DoubleVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=1, padx=1, pady=1)

        self.label2=ttk.Label(self.lf1, text="y")
        self.label2.grid(column=2,row=1, padx=1, pady=1)

        self.dato2=tk.DoubleVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=3, row=1, padx=5, pady=5)
        ##
        self.boton1=ttk.Button(self.lf1, text="Aplicar cambios", command=self.grafico_barra)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()

    def grafico_barra(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())
        if valor1>valor2 and valor1>valor3:
            mayor=valor1
        else:
            if valor2>valor3:
                mayor=valor2
            else:
                mayor=valor3
        largo1=valor1/mayor*400
        largo2=valor2/mayor*400
        largo3=valor3/mayor*400
        self.canvas1.create_rectangle(10,10,10+largo1,90,fill="red")
        self.canvas1.create_rectangle(10,120,10+largo2,200,fill="blue")
        self.canvas1.create_rectangle(10,230,10+largo3,310,fill="green")
        self.canvas1.create_text(largo1+70, 50, text="partido A", fill="white", font="Arial")
        self.canvas1.create_text(largo2+70, 160, text="partido B", fill="white", font="Arial")
        self.canvas1.create_text(largo3+70, 270, text="partido C", fill="white", font="Arial")
        

aplicacion1=Aplicacion()