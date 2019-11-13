import tkinter as tk
from tkinter import ttk
import numpy as np
import math 
from copy import deepcopy 

class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()
		self.entradadatos()
		self.canvas1=tk.Canvas(self.ventana1, width=1000, height=800, background="black")
		self.canvas1.grid(column=0, row=0)

		self.points = [[118, 345],[118, 138],[436, 345],[436,138],[268,75],[218,345],[298,345],[298,240],[218,240]]
		self.med_casa = []
		self.casa()
		self.ventana1.mainloop()

	
	def change_origin(self,y):
		return self.canvas1.winfo_height() - y

	def casa(self):	
		
		group=[]
		group.append(self.create_l(self.points[0],self.points[1]))
		group.append(self.create_l(self.points[0],self.points[2]))
		group.append(self.create_l(self.points[2],self.points[3]))
		group.append(self.create_l(self.points[1],self.points[3]))
		group.append(self.create_l(self.points[1],self.points[4]))
		group.append(self.create_l(self.points[4],self.points[3]))
		#puerta
		group.append(self.create_l(self.points[5],self.points[8]))
		group.append(self.create_l(self.points[6],self.points[7]))
		group.append(self.create_l(self.points[7],self.points[8]))
		
		self.med_casa = self.median_group(group)
		self.canvas1.create_line(self.med_casa[0]-2,self.med_casa[1],self.med_casa[0]+2,self.med_casa[1],width=3,fill="red")

	def median_line(self,l):
		m = np.median(l, axis = 0)
		m_x = int(m[0])
		m_y = int(m[1])
		return [m_x,m_y]
	
	def median_group(self,g):
		r = []
		for line in g:
			r.append(self.median_line(line))
		m = np.median(r, axis = 0)
		m_x = int(m[0])
		m_y = int(m[1])
		return [m_x,m_y]

	def entradadatos(self):
		self.lf1=ttk.LabelFrame(self.ventana1,text="Transformaciones 2D")
		self.lf1.grid(column=1, row=0, sticky="w")
	   
		# Trasladar #
		self.label1=ttk.Label(self.lf1, text="Trasladar")
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
		
		# Escalar #
		self.label3=ttk.Label(self.lf1, text="Escalar")
		self.label3.grid(column=0,row=2, padx=5, pady=5)

		self.label3=ttk.Label(self.lf1, text="x")
		self.label3.grid(column=0,row=3, padx=1, pady=1)

		self.dato3=tk.DoubleVar()
		self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
		self.entry3.grid(column=1, row=3, padx=1, pady=1)

		self.label4=ttk.Label(self.lf1, text="y")
		self.label4.grid(column=2,row=3, padx=1, pady=1)

		self.dato4=tk.DoubleVar()
		self.entry4=ttk.Entry(self.lf1, textvariable=self.dato4)
		self.entry4.grid(column=3, row=3, padx=5, pady=5)

		# Rotar #
		self.label5=ttk.Label(self.lf1, text="Rotar")
		self.label5.grid(column=0,row=4, padx=5, pady=5)
		
		self.label6=ttk.Label(self.lf1, text="º")
		self.label6.grid(column=0,row=5, padx=5, pady=5)
		
		self.dato5=tk.DoubleVar()
		self.entry5=ttk.Entry(self.lf1, textvariable=self.dato5)
		self.entry5.grid(column=1, row=5, padx=1, pady=1)

		# Shearing #
		self.label7=ttk.Label(self.lf1, text="Cizalladura")
		self.label7.grid(column=0,row=6, padx=5, pady=5)

		self.label7=ttk.Label(self.lf1, text="x")
		self.label7.grid(column=0,row=7, padx=1, pady=1)

		self.dato6=tk.DoubleVar()
		self.entry6=ttk.Entry(self.lf1, textvariable=self.dato6)
		self.entry6.grid(column=1, row=7, padx=1, pady=1)

		self.label8=ttk.Label(self.lf1, text="y")
		self.label8.grid(column=2,row=7, padx=1, pady=1)

		self.dato7=tk.BooleanVar()
		self.entry7=ttk.Entry(self.lf1, textvariable=self.dato7)
		self.entry7.grid(column=3, row=7, padx=5, pady=5)

		# Reflect #
		self.label7=ttk.Label(self.lf1, text="Reflejar")
		self.label7.grid(column=0,row=8, padx=5, pady=5)
		self.dato8=tk.DoubleVar()
		self.r1 = ttk.Radiobutton(self.lf1, text="Option 1", variable=self.dato8, value=True)
		self.r1.grid(column=0,row=9, padx=5, pady=5)
		self.r2 = ttk.Radiobutton(self.lf1, text="Option 2", variable=self.dato8, value=False)
		self.r2.grid(column=1,row=9, padx=5, pady=5)
		self.r3 = ttk.Radiobutton(self.lf1, text="Option 3", variable=self.dato8, value=3)
		self.r3.grid(column=2,row=9, padx=5, pady=5)
		

		self.boton1=ttk.Button(self.lf1, text="Aplicar cambios", command=self.reflexion)
		self.boton1.grid(column=0, row=10, columnspan=2, padx=5, pady=5, sticky="we")
		self.entry1.focus()

	def create_l(self,p1,p2):
		self.L=[]
		self.bresenham_real_mod(p1,p2)
		for p in self.L:
			self.canvas1.create_line(p[0],p[1],p[0]+1,p[1],fill="gold")
		return self.L

	def bresenham_real_mod(self,p1,p2):
		x1, y1, x2, y2 = int(p1[0]),int(p1[1]),int(p2[0]),int(p2[1])
		
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
		
		
	def translate(self,x = None,y = None):
		self.canvas1.delete(tk.ALL)

		x = self.dato1.get() #- self.med_casa[0]
		y = self.dato2.get() #- self.med_casa[1]
		self.L_aux=np.asarray(self.points)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,0,x],[0,1,y],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.points=np.array(self.L_aux).tolist() 

		self.casa()

	
	def escale(self):
		self.canvas1.delete(tk.ALL)
		
		sx = self.dato3.get() 
		sy = self.dato4.get()

		coordinate_aux = self.med_casa
		#self.translate(0,0)
		self.L_aux=np.asarray(self.points)
		
		self.L_aux=np.subtract(self.L_aux,self.med_casa)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1 = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
		self.L_aux = aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.add(self.L_aux,self.med_casa)
		self.points = np.array(self.L_aux).tolist()
		
		#self.translate(coordinate_aux[0],coordinate_aux[1])
		
		self.casa()

	def rotate(self):
		self.canvas1.delete(tk.ALL)
		
		alpha = self.dato5.get() 
		
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		coordinate_aux = self.med_casa
		for i in range(len(self.points)):
			self.points[i][1] = self.change_origin(self.points[i][1])
		self.L_aux=np.asarray(self.points)
		self.L_aux=np.subtract(self.L_aux,self.med_casa)

		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))

		cos_alpha = math.cos(math.radians(alpha))
		sen_alpha = math.sin(math.radians(alpha))
		aux1=np.array([[cos_alpha,sen_alpha,0],[-sen_alpha,cos_alpha,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,self.med_casa)
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		self.points = np.array(self.L_aux).tolist()
		for i in range(len(self.points)):
			self.points[i][1] = self.change_origin(self.points[i][1])
		self.casa()
		#self.translation(coordinate_aux[0],coordinate_aux[1])

	def shearing(self):
		self.canvas1.delete(tk.ALL)
		
		cx = self.dato6.get() 
		cy = self.dato7.get()


		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		coordinate_aux = self.med_casa
		for i in range(len(self.points)):
			self.points[i][1] = self.change_origin(self.points[i][1])
		self.L_aux=np.asarray(self.points)
		self.L_aux=np.subtract(self.L_aux,self.med_casa)


		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,cx,0],[cy,1,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,self.med_casa)
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		self.points = np.array(self.L_aux).tolist()
		for i in range(len(self.points)):
			self.points[i][1] = self.change_origin(self.points[i][1])
		self.casa()

	def reflexion(self):
		#reflect_x_or_y = true then refleclt x else reflect y
		self.canvas1.delete(tk.ALL)
		
		reflect_x_or_y = self.dato8.get() 
		
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		coordinate_aux = self.med_casa
		for i in range(len(self.points)):
			self.points[i][1] = self.change_origin(self.points[i][1])
		self.L_aux=np.asarray(self.points)
		self.L_aux=np.subtract(self.L_aux,self.med_casa)

		
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		if reflect_x_or_y:
			aux1=np.array([[1,0,0],[0,-1,0],[0,0,1]])
		else:
			aux1=np.array([[-1,0,0],[0,1,0],[0,0,1]])

		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,self.med_casa)
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		self.points = np.array(self.L_aux).tolist()
		for i in range(len(self.points)):
			self.points[i][1] = self.change_origin(self.points[i][1])
		self.casa()

aplicacion1=Aplicacion()