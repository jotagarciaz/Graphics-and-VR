import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import numpy as np
import copy
import math
import random

class Aplicacion(tk.Tk):
	def __init__(self):
		self.ventana1=tk.Tk()
		self.height = 480
		self.width = 1000
		self.margin = 20
		self.fern_matrix = [[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
							[0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
							[0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
							[-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]

		self.jgarciaz = [
						[0.1,0,0,0.1,-6,8,0.03225806452], #J top
						[0,0.08,-0.24,0,-4.5,6.1,0.03225806452], #J v
						[0.08,0,0,0.1,-6,-0.8,0.03225806452], # J bot

						[0.1,0,0,0.1,-2,8,0.03225806452], #G top
						[0,0.08,-0.24,0,-2.6,6.1,0.03225806452], #G v l
						[0.1,0,0,0.1,-2,-0.8,0.03225806452],	#G bot
						[0, 0.06, -0.1, 0, -0.1, 2.6, 0.03225806452], #G v r
						[0.06, 0, 0, 0.06, -1, 3.5, 0.03225806452],# G v mid

						[0.1, 0, 0, 0.1, 2, 8, 0.03225806452], # A top
						[0,0.08,-0.28,0,1.4,6,0.03225806452], # A v l
						[0,0.08,-0.28,0,3.8,6,0.03225806452], # A vertical right
						[0.05, 0, 0, 0.06, 2.5, 3.6, 0.03225806452], # A mid

						[0.1,0,0,0.1,6,8,0.03225806452],#R top
						[0,0.08,-0.28,0,5.4,6.0,0.03225806452],#R v left
						[0,0.08,-0.16,0,8,7.0,0.03225806452],#R v r
						[0.06, 0, 0, 0.06, 6.5, 3.6, 0.03225806452],#R mid
						[0.065,0.05,-0.12,0.065,6.8,2,0.03225806452],#R angle

						[0.1, 0, 0, 0.1, 10, 8, 0.03225806452],#C top
						[0,0.08,-0.24,0,9.4,6.1,0.03225806452],#C v 
						[0.1, 0, 0, 0.1, 10, -0.8, 0.03225806452],#C bot
						

						[0.1, 0, 0, 0.1, 14, 8, 0.03225806452],#I  top
						[0,0.08,-0.24,0,14.5,6.1,0.03225806452],#I v
						[0.1, 0, 0, 0.1, 14, -0.8, 0.03225806452],#I bot 
						

						[0.1, 0, 0, 0.1, 18, 8, 0.03225806452], # A top
						[0,0.08,-0.28,0,17.4,6,0.03225806452], # A V left
						[0.05, 0, 0, 0.06, 18.5, 3.6, 0.03225806452], # A mid
						[0,0.08,-0.28,0,19.8,6,0.03225806452], # A V right
						


						[0.1, 0, 0, 0.1, 22, 8, 0.03225806452],#Z top
						[-0.065,0.05,-0.2,-0.06,23.5,6.1,0.03225806452], #Z angle
						[0.1, 0, 0, 0.1,22, -0.8, 0.03225806452]]#Z bot
		self.images = [] #type: list
		self.ventana1.geometry('1000x800')
		self.entradadatos()
		self.canvas1=tk.Canvas(self.ventana1, width=self.width+2*self.margin, height=self.height+2*self.margin, background="white")
		self.canvas1.grid(column=0, row=1)
		self.points = [] #type: list
		self.draw()
		self.ventana1.mainloop()
		self.matrix = []
	def origin(self, y_coordinate):
		y_coordinate = self.canvas1.winfo_height() - y_coordinate
		return y_coordinate

	def entradadatos(self):
		self.lf1=ttk.LabelFrame(self.ventana1, text="Choose your fractal.")
		self.lf1.grid(column=0, row=0)
		self.label1=ttk.Label(self.lf1, text="Recursive fractals:")
		self.label1.grid(column=0,row=0, padx=5, pady=5)
		self.dato=tk.IntVar()
		self.triangle = ttk.Radiobutton(self.lf1, text="Sierpinsky's Triangle", variable=self.dato, value=1, command=self.passing_parameters)
		self.triangle.grid(column=0,row=1, padx=5, pady=5)
		self.carpet = ttk.Radiobutton(self.lf1, text="Sierpinsky's Carpet", variable=self.dato, value=2, command=self.passing_parameters)
		self.carpet.grid(column=0,row=2, padx=5, pady=5)
		self.koch = ttk.Radiobutton(self.lf1, text="Koch's Curve", variable=self.dato, value=3, command=self.passing_parameters)
		self.koch.grid(column=0,row=3, padx=5, pady=5)
		self.label2 = ttk.Label(self.lf1, text="Level")
		self.label2.grid(column=1,row=1, padx=5, pady=5)
		self.level=tk.IntVar()
		self.level=ttk.Entry(self.lf1, textvariable=self.level, width=3, justify=tk.CENTER)
		self.level.grid(column=1, row=2, padx=5, pady=5)
		self.level.insert(tk.INSERT, "1")
		self.label3=ttk.Label(self.lf1, text="IFS fractals:")
		self.label3.grid(column=2, row=0, padx=5, pady=5)
		self.fern = ttk.Radiobutton(self.lf1, text="Fern's IFS", variable=self.dato, value=4, command=self.passing_parameters)
		self.fern.grid(column=2, row=1, padx=5, pady=5)
		self.choose_ifs = ttk.Radiobutton(self.lf1, text="Choose your IFS", variable=self.dato, value=5, command=self.passing_parameters)
		self.choose_ifs.grid(column=2, row=2, padx=5, pady=5)
		self.clara_ifs = ttk.Radiobutton(self.lf1, text="JGARCIAZ", variable=self.dato, value=8, command=self.passing_parameters)
		self.clara_ifs.grid(column=2, row=3, padx=5, pady=5)
		self.labelParameters = ttk.Label(self.lf1, text="Parameters:")
		self.labelA = ttk.Label(self.lf1, text="A")
		self.A=tk.DoubleVar()
		self.A=ttk.Entry(self.lf1, textvariable=self.A, width=3, justify=tk.CENTER)
		self.A.insert(tk.INSERT, "0.5")
		self.labelB = ttk.Label(self.lf1, text="B")
		self.B=tk.DoubleVar()
		self.B=ttk.Entry(self.lf1, textvariable=self.B, width=3, justify=tk.CENTER)
		self.B.insert(tk.INSERT, "0.")
		self.labelC = ttk.Label(self.lf1, text="C")
		self.C=tk.DoubleVar()
		self.C=ttk.Entry(self.lf1, textvariable=self.C, width=3, justify=tk.CENTER)
		self.C.insert(tk.INSERT, "0.")
		self.labelD = ttk.Label(self.lf1, text="D")
		self.D=tk.DoubleVar()
		self.D=ttk.Entry(self.lf1, textvariable=self.D, width=3, justify=tk.CENTER)
		self.D.insert(tk.INSERT, "0.5")
		self.labelE = ttk.Label(self.lf1, text="E")
		self.E=tk.DoubleVar()
		self.E=ttk.Entry(self.lf1, textvariable=self.E, width=3, justify=tk.CENTER)
		self.E.insert(tk.INSERT, "1")
		self.labelF = ttk.Label(self.lf1, text="F")
		self.F=tk.DoubleVar()
		self.F=ttk.Entry(self.lf1, textvariable=self.F, width=3, justify=tk.CENTER)
		self.F.insert(tk.INSERT, "1")
		self.labelP = ttk.Label(self.lf1, text="P")
		self.P=tk.DoubleVar()
		self.P=ttk.Entry(self.lf1, textvariable=self.P, width=3, justify=tk.CENTER)
		self.P.insert(tk.INSERT, "0.33")
		self.botonM=ttk.Button(self.lf1, text="Add", command=self.add_row, width=4)

		self.label4=ttk.Label(self.lf1, text="Set fractals:")
		self.label4.grid(column=4, row=0, padx=5, pady=5)
		self.mandelbrot = ttk.Radiobutton(self.lf1, text="Mandelbrot", variable=self.dato, value=6, command=self.passing_parameters)
		self.mandelbrot.grid(column=4, row=1, padx=5, pady=5)
		self.julia = ttk.Radiobutton(self.lf1, text="Julia", variable=self.dato, value=7, command=self.passing_parameters)
		self.julia.grid(column=4, row=2, padx=5, pady=5)
		self.CReal = ttk.Label(self.lf1, text="C real")
		self.creal=tk.DoubleVar()
		self.creal=ttk.Entry(self.lf1, textvariable=self.creal, width=4, justify=tk.CENTER)
		self.creal.insert(tk.INSERT, "-0.65")
		self.CImaginary = ttk.Label(self.lf1, text="C imaginary")
		self.cimaginary=tk.DoubleVar()
		self.cimaginary=ttk.Entry(self.lf1, textvariable=self.cimaginary, width=4, justify=tk.CENTER)
		self.cimaginary.insert(tk.INSERT, "0.42")
		self.boton1=ttk.Button(self.lf1, text="Apply", command=self.draw)
		self.boton1.grid(column=0, row=6, columnspan=2, padx=5, pady=5, sticky="we")

	def add_row(self):
		self.matrix.append([float(self.A.get()), float(self.B.get()), float(self.C.get()), float(self.D.get()), float(self.E.get()), float(self.F.get()), float(self.P.get())])

	def passing_parameters(self):
		if self.dato.get() == 5:
			self.labelParameters.grid(column=3, row=0, padx=5, pady=5)
			self.labelA.grid(column=3, row=1, padx=5, pady=5)
			self.A.grid(column=4, row=1, padx=5, pady=5)
			self.labelB.grid(column=3, row=2, padx=5, pady=5)
			self.B.grid(column=4, row=2, padx=5, pady=5)
			self.labelC.grid(column=3, row=3, padx=5, pady=5)
			self.C.grid(column=4, row=3, padx=5, pady=5)
			self.labelD.grid(column=5, row=1, padx=5, pady=5)
			self.D.grid(column=6, row=1, padx=5, pady=5)
			self.labelE.grid(column=5, row=2, padx=5, pady=5)
			self.E.grid(column=6, row=2, padx=5, pady=5)
			self.labelF.grid(column=5, row=3, padx=5, pady=5)
			self.F.grid(column=6, row=3, padx=5, pady=5)
			self.labelP.grid(column=3, row=4, padx=5, pady=5)
			self.P.grid(column=4, row=4, padx=5, pady=5)
			self.botonM.grid(column=6, row=4, padx=5, pady=5)
			self.label4.grid(column=7, row=0, padx=5, pady=5)
			self.mandelbrot.grid(column=7, row=1, padx=5, pady=5)
			self.julia.grid(column=7, row=2, padx=5, pady=5)
		elif self.dato.get() == 7:
			self.CReal.grid(column=4, row=3, padx=5, pady=5)
			self.creal.grid(column=5, row=3, padx=5, pady=5)
			self.CImaginary.grid(column=4, row=4, padx=5, pady=5)
			self.cimaginary.grid(column=5, row=4, padx=5, pady=5)
		else:
			self.labelParameters.grid_remove()
			self.labelA.grid_remove()
			self.A.grid_remove()
			self.labelB.grid_remove()
			self.B.grid_remove()
			self.labelC.grid_remove()
			self.C.grid_remove()
			self.labelD.grid_remove()
			self.D.grid_remove()
			self.labelE.grid_remove()
			self.E.grid_remove()
			self.labelF.grid_remove()
			self.F.grid_remove()
			self.labelP.grid_remove()
			self.P.grid_remove()
			self.label4.grid(column=4, row=0, padx=5, pady=5)
			self.mandelbrot.grid(column=4, row=1, padx=5, pady=5)
			self.julia.grid(column=4, row=2, padx=5, pady=5)
			self.CReal.grid_remove()
			self.creal.grid_remove()
			self.CImaginary.grid_remove()
			self.cimaginary.grid_remove()

	def draw(self):
		self.canvas1.delete("all")
		if self.dato.get() == 1:
			level = int(self.level.get())
			x1 = self.margin + 0 
			y1 = self.margin + self.height
			x2 = self.margin + self.width/2
			y2 = self.margin + 0
			x3 = self.margin + self.width
			y3 = self.margin + self.height
			self.sierp_triangle(level, x1, y1, x2, y2, x3, y3)
		elif self.dato.get() == 2:
			level = int(self.level.get())
			x1 = self.margin 
			y1 = self.margin
			x2 = self.width - self.margin 
			y2 = self.height - self.margin  
			self.sierp_carpet(level, x1, y1, x2, y2)
		elif self.dato.get() == 3:
			level = int(self.level.get())
			x1 = self.margin + 0 
			y1 = self.margin + self.height
			x4 = self.margin + self.width/2
			y4 = self.margin + 0
			self.koch_curve(level, x1, y1, x4, y4)
		elif self.dato.get() == 4:
			level = int(self.level.get())
			positionx = self.margin + self.width/2
			positiony = self.margin + self.height/2
			self.ifs(self.fern_matrix, positionx, positiony)
		elif self.dato.get() == 5:
			
			matrix = [[float(self.A.get()), float(self.B.get()), float(self.C.get()), float(self.D.get()), float(self.E.get()), float(self.F.get()), float(self.P.get())], [0.5, 0, 0, 0.5, -1, 1, 0.33], [0.5, 0, 0, 0.5, 0, -1, 0.33]]
			level = int(self.level.get())
			positionx = self.margin + self.width/2
			positiony = self.margin + self.height/2
			self.ifs(matrix, positionx, positiony)
		elif self.dato.get() == 6:
			positionx = self.margin + self.width/2
			positiony = self.margin + self.height/2
			self.mandelbrot_set(positionx, positiony)
		elif self.dato.get() == 7:
			positionx = self.margin + self.width/2
			positiony = self.margin + self.height/2
			self.julia_set(positionx, positiony)
		elif self.dato.get() == 8:
			positionx = self.margin + self.width/2
			positiony = self.margin + self.height/2
			self.ifs(self.jgarciaz, positionx, positiony)

	def sierp_triangle(self, level, x1, y1, x2, y2, x3, y3):
		if level <= 1:
			self.canvas1.create_line(x1, y1, x2, y2)
			self.canvas1.create_line(x2, y2, x3, y3)
			self.canvas1.create_line(x3, y3, x1, y1)
		else:
			level = level - 1
			middle_x1 = (x1 + x2)/2
			middle_y1 = (y1 + y2)/2
			middle_x2 = (x2 + x3)/2
			middle_y2 = (y2 + y3)/2
			middle_x3 = (x3 + x1)/2
			middle_y3 = (y3 + y1)/2
			self.sierp_triangle(level, x1, y1, middle_x1, middle_y1, middle_x3, middle_y3)
			self.sierp_triangle(level, middle_x1, middle_y1, x2, y2, middle_x2, middle_y2)
			self.sierp_triangle(level, middle_x3, middle_y3, middle_x2, middle_y2, x3, y3)

	def sierp_carpet(self, level, x1, y1, x2, y2):
		if level < 1:
			self.canvas1.create_rectangle(x1,y1,x2,y2, fill='black')
		else:
			level -=1
			x_0 = x1
			y_0 = y1
			x_02 = x2
			y_02 = y2
			x_1 = (x2/3) + ((x1/3)*2)
			y_1 = (y1/3) + ((y2/3)*2)
			x_2 = ((x2/3)*2) + (x1/3)
			y_2 = ((y1/3)*2) + (y2/3)
			self.sierp_carpet(level, x_0, y_0, x_1, y_2)
			self.sierp_carpet(level, x_1, y_0, x_2, y_2)
			self.sierp_carpet(level, x_2, y_0, x_02, y_2)
			self.sierp_carpet(level, x_0, y_2, x_1, y_1)
			self.sierp_carpet(level, x_2, y_2, x_02, y_1)
			self.sierp_carpet(level, x_0, y_1, x_1, y_02)
			self.sierp_carpet(level, x_1, y_1, x_2, y_02)
			self.sierp_carpet(level, x_2, y_1, x_02, y_02)

	def koch_curve(self, level, x1, y1, x4, y4):
		if level <= 1:
			self.canvas1.create_line(x1, y1, x4, y4)
		else:
			level = level - 1
			Dx = (x4 - x1) / 3
			Dy = (y4 - y1) / 3
			x2 = x1 + Dx
			y2 = y1 + Dy
			x3 = x2 + Dx
			y3 = y2 + Dy
			x = (Dx - math.sqrt(3) * Dy)/2 + (x1 + Dx)
			y = (math.sqrt(3) * Dx + Dy)/2 + (y1 + Dy)
			self.koch_curve(level, x1, y1, x2, y2)
			self.koch_curve(level, x2, y2, x, y)
			self.koch_curve(level, x, y, x3, y3)
			self.koch_curve(level, x3, y3, x4, y4)

	def ifs(self, matrix, positionx, positiony):
		if self.dato.get() == 8:
			imgx = 640
			imgy = 520
		else:
			imgx = self.margin + self.width
			imgy = self.margin + self.height
		x = matrix[0][4]
		y = matrix[0][5] 
		xa = x
		xb = x
		ya = y
		yb = y
		
		for k in range(imgx * imgy):
			p = random.random()
			psum = 0.0
			for i in range(len(matrix)):
				psum += matrix[i][6]
				if p <= psum:
					break
			x0 = x * matrix[i][0] + y * matrix[i][1] + matrix[i][4] 
			y  = x * matrix[i][2] + y * matrix[i][3] + matrix[i][5] 
			x = x0 
			if x < xa:
				xa = x
			if x > xb:
				xb = x
			if y < ya:
				ya = y
			if y > yb:
				yb = y
		if self.dato.get() == 8:
			imgy = round(imgy * (yb - ya) / (xb - xa))
		image = PhotoImage(width = imgx, height = imgy)
		self.canvas1.create_image(positionx, positiony, image=image)
		x=0.0
		y=0.0 
		image.put('white', to=(0, 0, imgx, imgy))
		for k in range(imgx * imgy):
			p=random.random() 
			psum = 0.0
			for i in range(len(matrix)):
				psum += matrix[i][6]
				if p <= psum:
					break
			x0 = x * matrix[i][0] + y * matrix[i][1] + matrix[i][4] 
			y  = x * matrix[i][2] + y * matrix[i][3] + matrix[i][5] 
			x = x0 
			jx = int((x - xa) / (xb - xa) * (imgx - 1)) 
			jy = (imgy - 1) - int((y - ya) / (yb - ya) * (imgy - 1))
			image.put('black', (jx, jy))
		self.canvas1.update()
		self.images.append(image)

	def mandelbrot_set(self, positionx, positiony):
		xa = -2.0; xb = 1.0
		ya = -1.5; yb = 1.5
		maxIt = 256

		img = PhotoImage(width = self.width+self.margin, height = self.height+self.margin)
		self.canvas1.create_image(positionx, positiony, image = img)
		for ky in range(self.height): #si haces hilos de Ky, cada hilo hace kx, lo que lo optimiza bastante
			for kx in range(self.width):
				c = complex(xa + (xb - xa) * kx / self.width, ya + (yb - ya) * ky / self.height)
				z = complex(0.0, 0.0)
				for i in range(maxIt):
					z = z * z + c
					if abs(z) >= 2.0:
						break
				rd = hex(i % 5 * 20)[2:].zfill(2)
				gr = hex(i % 6 * 5)[2:].zfill(2)
				bl = hex(i % 15 * 16)[2:].zfill(2)
				img.put("#" + rd + gr + bl, (kx, ky))
		self.canvas1.update()
		self.images.append(img)

	def julia_set(self, positionx, positiony):
		maxIt = 256

		real = np.linspace(-1.5, 1.5, self.width)
		imaginary = np.linspace(-1.0, 1.0, self.height)

		img = PhotoImage(width = self.width+self.margin, height = self.height+self.margin)
		self.canvas1.create_image(positionx, positiony, image = img)
		for ky in range(self.height): 
			for kx in range(self.width):
				c = complex(float(self.creal.get()), float(self.cimaginary.get()))
				z = complex(real[kx], imaginary[ky])
				for i in range(maxIt):
					z = z * z + c
					if abs(z) >= 2.0:
						break
				r = hex(i % 128)[2:].zfill(2)
				g = hex(i % 160)[2:].zfill(2)
				b = hex(i % 15 * 16)[2:].zfill(2)
				img.put("#" + r + g + b, (kx, ky))
		
		self.canvas1.update()
		self.images.append(img)

aplicacion1=Aplicacion()