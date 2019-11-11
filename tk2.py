import tkinter as tk
from tkinter import ttk
import numpy as np

class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()
		self.entradadatos()
		self.canvas1=tk.Canvas(self.ventana1, width=1000, height=800, background="black")
		self.canvas1.grid(column=0, row=0)

		self.points = [[118, 345],[118, 138],[436, 345],[436,138],[268,75],[218,345],[298,345],[298,240],[218,240]]

		self.casa()
		self.ventana1.mainloop()

	

	def casa(self):	
		
		
		self.create_l(self.points[0],self.points[1])
		self.create_l(self.points[0],self.points[2])
		self.create_l(self.points[2],self.points[3])
		self.create_l(self.points[1],self.points[3])
		self.create_l(self.points[1],self.points[4])
		self.create_l(self.points[4],self.points[3])
		#puerta
		self.create_l(self.points[5],self.points[8])
		self.create_l(self.points[6],self.points[7])
		self.create_l(self.points[7],self.points[8])
		

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
		self.boton1=ttk.Button(self.lf1, text="Aplicar cambios", command=self.translate)
		self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
		self.entry1.focus()

	def create_l(self,p1,p2):
		self.L=[]
		self.bresenham_real_mod(p1,p2)
		for p in self.L:
			self.canvas1.create_line(p[0],p[1],p[0]+1,p[1],fill="gold")

	def bresenham_real_mod(self,p1,p2):
		x1, y1, x2, y2 = p1[0],p1[1],p2[0],p2[1]
		
		x = x1
		y = y1
		aux_dx = x2 - x1
		aux_dy = y2 - y1
		dx = abs(aux_dx)
		dy = abs(aux_dy)
		

		if dx == 0 or dy > dx:
			m = dx/dy
			e = m - 1/2
			i = 0
			while i <= dy:
				self.L.append([x,y])
				while e > 0:
					x = x + 1
					e = e - 1
				y = y + 1
				e = e + m
				i = i + 1
		else:
			m=dy/dx
			e = m - 1/2
			i = 0
			while i <= dx:
				self.L.append([x,y])
				while e > 0:
					y = y + 1
					e = e - 1
				x = x + 1
				e = e + m
				i = i + 1

		self.L=np.asarray(self.L)
		self.transform_quadrant(aux_dx, aux_dy)
		
		if self.L[0][0]<0:
			x1=2*x1
			self.L[...,0] +=x1
		if self.L[0][1]<0:
			y1=2*y1
			self.L[...,1] +=y1
		self.L=np.array(self.L).tolist()   

	
	def transform_quadrant(self,dx,dy):

		if dx>=0 and dy>=0:
			return self.L
		elif dx<0 and dy>=0:
			self.L=self.L.dot(np.array([[-1,0],[0,1]]))   
		elif dx<0 and dy<0:
			self.L=self.L.dot(np.array([[-1,0],[0,-1]]))
		elif dx>=0 and dy<0:
			self.L=self.L.dot(np.array([[1,0],[0,-1]]))
		
		
	def translate(self):
		self.canvas1.delete(tk.ALL)
		
		x = self.dato1.get() 
		y = self.dato2.get()

		#x = self.dato1.get() - self.points[0][0]
		#y = self.dato2.get() - self.points[0][1]
		self.L_aux=np.asarray(self.points)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,0,x],[0,1,y],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.points=np.array(self.L_aux).tolist() 

		self.casa()
		
	   

aplicacion1=Aplicacion()