import tkinter as tk
from tkinter import ttk
import numpy as np
import copy
import math

class Aplicacion(tk.Tk):
	def __init__(self):
		self.ventana1=tk.Tk()
		self.height = 512
		self.width = 640
		self.margin = 20
		self.ventana1.geometry('1000x800')
		self.entradadatos()
		self.canvas1=tk.Canvas(self.ventana1, width=self.width+2*self.margin, height=self.height+2*self.margin, background="white")
		self.canvas1.grid(column=0, row=1)
		self.points = [] #type: list
		self.draw()
		self.ventana1.mainloop()

	def origin(self, y_coordinate):
		y_coordinate = self.canvas1.winfo_height() - y_coordinate
		return y_coordinate

	def entradadatos(self):
		self.lf1=ttk.LabelFrame(self.ventana1, text="Choose your fractal.")
		self.lf1.grid(column=0, row=0)
		self.label1=ttk.Label(self.lf1, text="Recursive fractals:")
		self.label1.grid(column=0,row=0, padx=5, pady=5)
		self.dato=tk.IntVar()
		self.triangle = ttk.Radiobutton(self.lf1, text="Sierpinsky's Triangle", variable=self.dato, value=1)
		self.triangle.grid(column=0,row=1, padx=5, pady=5)
		self.carpet = ttk.Radiobutton(self.lf1, text="Sierpinsky's Carpet", variable=self.dato, value=2)
		self.carpet.grid(column=0,row=2, padx=5, pady=5)
		self.koch = ttk.Radiobutton(self.lf1, text="Koch's Curve", variable=self.dato, value=3)
		self.koch.grid(column=0,row=3, padx=5, pady=5)
		self.label2 = ttk.Label(self.lf1, text="Level")
		self.label2.grid(column=1,row=1, padx=5, pady=5)
		self.level=tk.IntVar()
		self.level=ttk.Entry(self.lf1, textvariable=self.level, width=3, justify=tk.CENTER)
		self.level.grid(column=1, row=2, padx=5, pady=5)
		self.level.insert(tk.INSERT, "1")
		self.boton1=ttk.Button(self.lf1, text="Transform", command=self.draw)
		self.boton1.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky="we")

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

	def sierp_triangle(self, level, x1, y1, x2, y2, x3, y3):
		if level <= 1:
			#print("   draw element")
			self.canvas1.create_line(x1, y1, x2, y2)
			self.canvas1.create_line(x2, y2, x3, y3)
			self.canvas1.create_line(x3, y3, x1, y1)
		else:
			#print("   recursion")
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

aplicacion1=Aplicacion()