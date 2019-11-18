import tkinter as tk
from tkinter import ttk
import numpy as np
import math 
from copy import deepcopy 
import time

class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()

		self.canvas1=tk.Canvas(self.ventana1, width=1000, height=800, background="black")
		self.canvas1.grid(column=0, row=0)
		
		self.reflected_or_rotated = False
		self.points = [[118, 345],[118, 138],[436, 345],[436,138],[268,75],[218,345],[298,345],[298,240],[218,240]]
		self.med_casa = []
		self.animation()
		self.ventana1.mainloop()
		
	
	def change_origin(self,y):
		return self.canvas1.winfo_height() - y

	def casa(self):	
		
		group_casa=[]
		group_casa.append(self.create_l(self.points[0],self.points[1]))
		group_casa.append(self.create_l(self.points[0],self.points[2]))
		group_casa.append(self.create_l(self.points[2],self.points[3]))
		group_casa.append(self.create_l(self.points[1],self.points[3]))
		group_casa.append(self.create_l(self.points[1],self.points[4]))
		group_casa.append(self.create_l(self.points[4],self.points[3]))
		#puerta
		group_casa.append(self.create_l(self.points[5],self.points[8]))
		group_casa.append(self.create_l(self.points[6],self.points[7]))
		group_casa.append(self.create_l(self.points[7],self.points[8]))
		if not self.reflected_or_rotated:
			self.med_casa = self.median_group(group_casa)
		else:
			self.reflected_or_rotated=False
		
	def animation(self):
		self.casa()

		for i in range(0,8):
			time.sleep(0.1)
			self.points=self.rotate(self.points,45)
			self.points=self.escale(self.points,0.75,0.75)
			self.casa()
			self.canvas1.update()

				
		
	
	def median_group(self,g):
		r = []
		for line in g:
			m = np.amin(line, axis = 0)
			mm = np.amax(line, axis = 0)
			m_x = int(m[0])
			m_y = int(m[1])
			mm_x = int(mm[0])
			mm_y = int(mm[1])
			r.append([m_x,m_y])
			r.append([mm_x,mm_y])
		m = np.amin(r, axis = 0)
		mm = np.amax(r, axis = 0)
		
		return [(mm[0]+m[0])/2,(mm[1]+m[1])/2]

	

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
		
		
	def translate(self,group,x = 0,y = 0):
		self.canvas1.delete(tk.ALL)

		self.L_aux=np.asarray(group)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,0,x],[0,1,y],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		group=np.array(self.L_aux).tolist() 
		return group
		

	
	def escale(self,group,sx = 1 , sy = 1):
		self.canvas1.delete(tk.ALL)
	
		coordinate_aux = self.med_casa
		#self.translate(0,0)
		self.L_aux=np.asarray(group)
		
		self.L_aux=np.subtract(self.L_aux,self.med_casa)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1 = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
		self.L_aux = aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.add(self.L_aux,self.med_casa)
		group = np.array(self.L_aux).tolist()
		return group
		#self.translate(coordinate_aux[0],coordinate_aux[1])
		
		

	def rotate(self,group,alpha = 45):
		self.canvas1.delete(tk.ALL)
				
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))

		coordinate_aux = self.med_casa
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
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

		group= np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.reflected_or_rotated = True
		#self.translation(coordinate_aux[0],coordinate_aux[1])
		return group

	def shearing(self, group ,cx = 0 ,cy = 0):
		self.canvas1.delete(tk.ALL)
		
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		coordinate_aux = self.med_casa
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,self.med_casa)


		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,cx,0],[cy,1,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,self.med_casa)
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		group = np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		return group

	def reflexion(self,reflexion_type = 1,rotate_degrees = None):
		
		#reflexion_type = 1 then reflect x, 2 reflect y , 3 reflect on degree line, that pass through origin
		self.canvas1.delete(tk.ALL)
		
		if reflexion_type == 3:
			self.rotate(rotate_degrees)

		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,self.med_casa)

		
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		
		if reflexion_type == 1 or reflexion_type == 3:
			aux1=np.array([[1,0,0],[0,-1,0],[0,0,1]])
		elif reflexion_type == 2:
			aux1=np.array([[-1,0,0],[0,1,0],[0,0,1]])	
	
			
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		

		self.L_aux=np.add(self.L_aux,self.med_casa)
		self.med_casa[1] = deepcopy(self.change_origin(self.med_casa[1]))
		
		group = np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		
		if reflexion_type == 3 != 0:
			self.rotate(-rotate_degrees)
			self.reflected_or_rotated = True
		
		

aplicacion1=Aplicacion()