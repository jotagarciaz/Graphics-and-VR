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
		self.bucket_list = [[300,545],[315,564],[338,570],[585,570],[615,565],[635,550],[660,270],[270,270],[270,240],[660,240],[670,235],[660,225],[275,225],[265,235],[275,240], [295,485],[385,485],[370,240], [640,485],[550,485],[560,240]]
																																													#K			#F																																										#C	
		self.letters_list = [[415,540],[418,530],[420,510],[418,510],[418,505],[435,505],[430,520],[440,510],[440,505],[458,505],[458,510],[440,525],[454,540],[435,540],[430,530],[430,540],[410,540],  [457,540],[459,525],[462,510],[459,510],[459,505],[490,505],[490,515],[485,515],[485,512],[475,512],[475,520],[480,520],[480,530],[470,530],[470,538],[475,540],[460,540], [520,540],[495,540],[490,530],[490,520],[495,512],[505,505],[525,505],[525,520],[520,520],[520,515],[510,515],[505,518],[502,530],[520,535]]
		self.coronel_sanders_list = []
		
		self.med_bucket = []
		self.med_letters = []
		self.med_coronel_sanders = []
		#self.animation()
		self.coronel_sanders()
		self.ventana1.mainloop()
		
	
	def change_origin(self,y):
		return self.canvas1.winfo_height() - y

	def bucket(self):	
		group_bucket=[]
		#bucket
		group_bucket.append(self.create_l(self.bucket_list[0],self.bucket_list[1]))
		group_bucket.append(self.create_l(self.bucket_list[1],self.bucket_list[2]))
		group_bucket.append(self.create_l(self.bucket_list[2],self.bucket_list[3]))
		group_bucket.append(self.create_l(self.bucket_list[3],self.bucket_list[4]))
		group_bucket.append(self.create_l(self.bucket_list[4],self.bucket_list[5]))
		group_bucket.append(self.create_l(self.bucket_list[5],self.bucket_list[6]))
		group_bucket.append(self.create_l(self.bucket_list[6],self.bucket_list[7]))
		group_bucket.append(self.create_l(self.bucket_list[0],self.bucket_list[7]))
		group_bucket.append(self.create_l(self.bucket_list[7],self.bucket_list[8]))
		group_bucket.append(self.create_l(self.bucket_list[8],self.bucket_list[9]))
		group_bucket.append(self.create_l(self.bucket_list[6],self.bucket_list[9]))
		group_bucket.append(self.create_l(self.bucket_list[9],self.bucket_list[10]))
		group_bucket.append(self.create_l(self.bucket_list[10],self.bucket_list[11]))
		group_bucket.append(self.create_l(self.bucket_list[11],self.bucket_list[12]))
		group_bucket.append(self.create_l(self.bucket_list[12],self.bucket_list[13]))
		group_bucket.append(self.create_l(self.bucket_list[13],self.bucket_list[8]))
		group_bucket.append(self.create_l(self.bucket_list[15],self.bucket_list[16]))
		group_bucket.append(self.create_l(self.bucket_list[16],self.bucket_list[17]))
		group_bucket.append(self.create_l(self.bucket_list[18],self.bucket_list[19]))
		group_bucket.append(self.create_l(self.bucket_list[19],self.bucket_list[20]))

		if not self.reflected_or_rotated:
			self.med_bucket = self.median_group(group_bucket)
		else:
			self.reflected_or_rotated=False
	
	def letters(self):	
		group_letters=[]
		#K
		group_letters.append(self.create_l(self.letters_list[0],self.letters_list[1]))
		group_letters.append(self.create_l(self.letters_list[1],self.letters_list[2]))
		group_letters.append(self.create_l(self.letters_list[2],self.letters_list[3]))
		group_letters.append(self.create_l(self.letters_list[3],self.letters_list[4]))
		group_letters.append(self.create_l(self.letters_list[4],self.letters_list[5]))
		group_letters.append(self.create_l(self.letters_list[5],self.letters_list[6]))
		group_letters.append(self.create_l(self.letters_list[6],self.letters_list[7]))
		group_letters.append(self.create_l(self.letters_list[7],self.letters_list[8]))
		group_letters.append(self.create_l(self.letters_list[8],self.letters_list[9]))
		group_letters.append(self.create_l(self.letters_list[9],self.letters_list[10]))
		group_letters.append(self.create_l(self.letters_list[10],self.letters_list[11]))
		group_letters.append(self.create_l(self.letters_list[11],self.letters_list[12]))
		group_letters.append(self.create_l(self.letters_list[12],self.letters_list[13]))
		group_letters.append(self.create_l(self.letters_list[13],self.letters_list[14]))
		group_letters.append(self.create_l(self.letters_list[14],self.letters_list[15]))
		group_letters.append(self.create_l(self.letters_list[15],self.letters_list[16]))
		#F
		group_letters.append(self.create_l(self.letters_list[17],self.letters_list[18]))
		group_letters.append(self.create_l(self.letters_list[18],self.letters_list[19]))
		group_letters.append(self.create_l(self.letters_list[19],self.letters_list[20]))
		group_letters.append(self.create_l(self.letters_list[20],self.letters_list[21]))
		group_letters.append(self.create_l(self.letters_list[21],self.letters_list[22]))
		group_letters.append(self.create_l(self.letters_list[22],self.letters_list[23]))
		group_letters.append(self.create_l(self.letters_list[23],self.letters_list[24]))
		group_letters.append(self.create_l(self.letters_list[24],self.letters_list[25]))
		group_letters.append(self.create_l(self.letters_list[25],self.letters_list[26]))
		group_letters.append(self.create_l(self.letters_list[26],self.letters_list[27]))
		group_letters.append(self.create_l(self.letters_list[27],self.letters_list[28]))
		group_letters.append(self.create_l(self.letters_list[28],self.letters_list[29]))
		group_letters.append(self.create_l(self.letters_list[29],self.letters_list[30]))
		group_letters.append(self.create_l(self.letters_list[30],self.letters_list[31]))
		group_letters.append(self.create_l(self.letters_list[31],self.letters_list[32]))
		group_letters.append(self.create_l(self.letters_list[32],self.letters_list[17]))
		#C
		
		group_letters.append(self.create_l(self.letters_list[34],self.letters_list[35]))
		group_letters.append(self.create_l(self.letters_list[35],self.letters_list[36]))
		group_letters.append(self.create_l(self.letters_list[36],self.letters_list[37]))
		group_letters.append(self.create_l(self.letters_list[37],self.letters_list[38]))
		group_letters.append(self.create_l(self.letters_list[38],self.letters_list[39]))
		group_letters.append(self.create_l(self.letters_list[39],self.letters_list[40]))
		group_letters.append(self.create_l(self.letters_list[40],self.letters_list[41]))
		group_letters.append(self.create_l(self.letters_list[41],self.letters_list[42]))
		group_letters.append(self.create_l(self.letters_list[42],self.letters_list[43]))
		group_letters.append(self.create_l(self.letters_list[43],self.letters_list[44]))
		group_letters.append(self.create_l(self.letters_list[44],self.letters_list[45]))
		group_letters.append(self.create_l(self.letters_list[45],self.letters_list[46]))
		group_letters.append(self.create_l(self.letters_list[46],self.letters_list[47]))
		group_letters.append(self.create_l(self.letters_list[47],self.letters_list[34]))
		
		
		if not self.reflected_or_rotated:
			self.med_letters = self.median_group(group_letters)
		else:
			self.reflected_or_rotated=False

	def coronel_sanders(self):
		group_coronel_sanders = []	
		group_coronel_sanders.append(self.create_l(self.coronel_sanders_list[0],self.coronel_sanders_list[1]))
		
		if not self.reflected_or_rotated:
			self.med_coronel_sanders = self.median_group(group_coronel_sanders)
		else:
			self.reflected_or_rotated=False		
	def animation(self):
		self.bucket()
		self.letters()
		

		for i in range(0,8):
			time.sleep(0.1)
			self.bucket_list=self.rotate(self.bucket_list,45)
			self.bucket_list=self.escale(self.bucket_list,0.9,0.9)
			self.letters_list=self.rotate(self.letters_list,45)
			self.letters_list=self.escale(self.letters_list,0.9,0.9)
			self.bucket()
			self.letters()
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
	
		coordinate_aux = self.med_bucket
		#self.translate(0,0)
		self.L_aux=np.asarray(group)
		
		self.L_aux=np.subtract(self.L_aux,self.med_bucket)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1 = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
		self.L_aux = aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.add(self.L_aux,self.med_bucket)
		group = np.array(self.L_aux).tolist()
		return group
		#self.translate(coordinate_aux[0],coordinate_aux[1])
		
		

	def rotate(self,group,alpha = 45):
		self.canvas1.delete(tk.ALL)
				
		self.med_bucket[1] = deepcopy(self.change_origin(self.med_bucket[1]))

		coordinate_aux = self.med_bucket
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,self.med_bucket)

		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))

		cos_alpha = math.cos(math.radians(alpha))
		sen_alpha = math.sin(math.radians(alpha))
		aux1=np.array([[cos_alpha,sen_alpha,0],[-sen_alpha,cos_alpha,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,self.med_bucket)

		self.med_bucket[1] = deepcopy(self.change_origin(self.med_bucket[1]))

		group= np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.reflected_or_rotated = True
		#self.translation(coordinate_aux[0],coordinate_aux[1])
		return group

	def shearing(self, group ,cx = 0 ,cy = 0):
		self.canvas1.delete(tk.ALL)
		
		self.med_bucket[1] = deepcopy(self.change_origin(self.med_bucket[1]))
		coordinate_aux = self.med_bucket
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,self.med_bucket)


		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,cx,0],[cy,1,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,self.med_bucket)
		self.med_bucket[1] = deepcopy(self.change_origin(self.med_bucket[1]))
		group = np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		return group

	def reflexion(self,reflexion_type = 1,rotate_degrees = None):
		
		#reflexion_type = 1 then reflect x, 2 reflect y , 3 reflect on degree line, that pass through origin
		self.canvas1.delete(tk.ALL)
		
		if reflexion_type == 3:
			self.rotate(rotate_degrees)

		self.med_bucket[1] = deepcopy(self.change_origin(self.med_bucket[1]))
		
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,self.med_bucket)

		
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		
		if reflexion_type == 1 or reflexion_type == 3:
			aux1=np.array([[1,0,0],[0,-1,0],[0,0,1]])
		elif reflexion_type == 2:
			aux1=np.array([[-1,0,0],[0,1,0],[0,0,1]])	
	
			
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		

		self.L_aux=np.add(self.L_aux,self.med_bucket)
		self.med_bucket[1] = deepcopy(self.change_origin(self.med_bucket[1]))
		
		group = np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		
		if reflexion_type == 3 != 0:
			self.rotate(-rotate_degrees)
			self.reflected_or_rotated = True
		
		

aplicacion1=Aplicacion()