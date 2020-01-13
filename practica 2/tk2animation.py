import tkinter as tk
from tkinter import ttk
import numpy as np
import math 
from copy import deepcopy 
import time
import pygame


class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()
		pygame.init()
		self.canvas1=tk.Canvas(self.ventana1, width=1000, height=800, background="gray99")
		self.canvas1.grid(column=0, row=0)
		self.reflected_or_rotated = False

		self.all_points = []
		self.bucket_list = [[300,545],[315,564],[338,570],[585,570],[615,565],[635,550],[660,270],[270,270],[270,240],[660,240],[670,235],[660,225],[275,225],[265,235],[275,240],         [295,485],[385,485],[370,240], [640,485],[550,485],[560,240],   [293,483],[641,483]]
																																											#K			#F																																										#C	
		self.letters_list = [[415,540],[418,530],[420,510],[418,510],[418,505],[435,505],[430,520],[440,510],[440,505],[458,505],[458,510],[440,525],[454,540],[435,540],[430,530],[430,540],[410,540],  [457,540],[459,525],[462,510],[459,510],[459,505],[490,505],[490,515],[485,515],[485,512],[475,512],[475,520],[480,520],[480,530],[470,530],[470,538],[475,540],[460,540], [520,540],[495,540],[490,530],[490,520],[495,512],[505,505],[525,505],[525,520],[520,520],[520,515],[510,515],[505,518],[502,530],[520,535]]
		self.coronel_sanders_list = [[455,478],[470,445],[450,445],[450,435],[460,435],[460,430],[440,400],[430,375],[425,370],[425,355],[425,345],[420,345],[420,335],[418,333],[418,325],[425,322],[425,317],[420,314],[424,310],[435,310],[434,305],[426,302],[437,301],[444,296],[444,291],[448,290],[448,288],[452,288],[453,285],[462,285],[464,283],[484,283],[483,285],[494,286],[520,310],[520,320],[525,320],[525,375],[516,385],[510,385],[510,400],[505,400],[505,410],[490,425],[485,425],[485,430],[496,433],[495,443],[478,443],[478,455],[480,455],[480,477],[475,475],[475,457],[470,458],[468,478]      ,     [433,307],[475,313],[454,314],[435,337],[435,382],[451,383],[468,379],[474,381],[488,376],[498,387],[492,395],[459,395],[449,384],[459,395],[462,428]     ,   [423,350],[435,355],[437,349],[460,348],[467,352],[478,353],[486,348],[516,350],[510,328],[525,360],[516,350],[507,350],  [505,364],[498,370],[494,370],[498,370],[505,364],[475,360],[475,353],[466,353],[466,357],[435,357],[437,366],[444,367],[445,369],[444,367],[437,366],[435,357],[466,357],[466,378],[466,365],[459,369],[458,380]]
		
								#Pollo1																															#Pollo4																												#Pollo3	mal																Pollo2
		self.chicken_1_list = [[295,220],[297,207],[298,198],[300,195],[300,190],[325,170],[330,168],[342,168],[344,172],[358,170],[358,177],[374,181],     [376,164],[375,183],[375,165],[392,148],[396,146],[410,145],[410,146],[418,152],[430,145],[450,146],[461,155],           [449,157],[435,156],[431,156], [418,162],[380,200],[375,219], 	      [375,220],[385,220],[395,202],[405,191],[425,189],[432,190],[449,205], [448,217],[444,221]      ,           [432,189],[475,140],[503,135],[545,145],[557,157],[573,180],   [485,222],[488,215],[510,196],[584,180],[587,183],[595,183],[600,175],[612,177],[623,190],[619,206],[600,221],   	[616,175],[640,153],[658,152],[675,169],[678,175],[677,188],[662,201],[659,212],[654,221]]							
		self.lagrima_list = [self.coronel_sanders_list[85],	[self.coronel_sanders_list[85][0]+3,self.coronel_sanders_list[85][1]+5]]																																						#Pollo5																#Pollo6																												#Pollo7
																																					 																													#principio ->						<-							
		self.all_points.extend(self.bucket_list)         
		self.all_points.extend(self.letters_list) 
		self.all_points.extend(self.coronel_sanders_list) 
		self.all_points.extend(self.chicken_1_list) 

		self.med_bucket = []
		self.med_letters = []
		self.med_coronel_sanders = []
		self.med_chicken_1 = []
		self.med_all = []
		self.med_lagrima = []

		#self.bucket()
		self.all_groups()
		self.animation()
		#self.coronel_sanders()
		#self.chicken1()
		#self.letters()
		self.ventana1.mainloop()
		
	
	def change_origin(self,y):
		return self.canvas1.winfo_height() - y

	def all_groups(self):
		

		divisions_low = 0
		divisions_top = len(self.bucket_list)
		self.bucket_list = self.all_points[divisions_low:divisions_top]
		self.bucket()
		
		divisions_low = divisions_top
		divisions_top += len(self.letters_list)
		self.letters_list = self.all_points[divisions_low:divisions_top]
		self.letters()

		divisions_low = divisions_top
		divisions_top += len(self.coronel_sanders_list)
		self.coronel_sanders_list = self.all_points[divisions_low:divisions_top]
		self.coronel_sanders()

		divisions_low = divisions_top
		divisions_top += len(self.chicken_1_list)
		if self.chicken_1_list:
			self.chicken_1_list = self.all_points[divisions_low:divisions_top]
			self.chicken1()

		
		if not self.reflected_or_rotated:
			self.med_all = self.median_all_groups(self.all_points)
		else:
			self.reflected_or_rotated=False

	def chicken1(self):
		group_chicken_1=[]

		for i in range(0,len(self.chicken_1_list)-1):
			group_chicken_1.append(self.create_l(self.chicken_1_list[i],self.chicken_1_list[i+1],color="DarkGoldenrod2",width=5))
		

		if not self.reflected_or_rotated:
			self.med_chicken_1 = self.median_group(group_chicken_1)
		else:
			self.reflected_or_rotated=False
		

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

		
		group_bucket.append(self.create_l(self.bucket_list[7],self.bucket_list[21],color="red",width=2))
		group_bucket.append(self.create_l(self.bucket_list[6],self.bucket_list[22],color="red",width=2))
		group_bucket.append(self.create_l(self.bucket_list[7],self.bucket_list[8],color="red",width=2))
		group_bucket.append(self.create_l(self.bucket_list[8],self.bucket_list[9]))
		group_bucket.append(self.create_l(self.bucket_list[6],self.bucket_list[9],color="red",width=2))
		group_bucket.append(self.create_l(self.bucket_list[9],self.bucket_list[10]))
		group_bucket.append(self.create_l(self.bucket_list[10],self.bucket_list[11]))
		group_bucket.append(self.create_l(self.bucket_list[11],self.bucket_list[12]))
		group_bucket.append(self.create_l(self.bucket_list[12],self.bucket_list[13]))
		group_bucket.append(self.create_l(self.bucket_list[13],self.bucket_list[8]))
		group_bucket.append(self.create_l(self.bucket_list[15],self.bucket_list[16],color="red",width=1))
		group_bucket.append(self.create_l(self.bucket_list[16],self.bucket_list[17],color="red",width=2))
		group_bucket.append(self.create_l(self.bucket_list[18],self.bucket_list[19],color="red",width=1))
		group_bucket.append(self.create_l(self.bucket_list[19],self.bucket_list[20],color="red",width=2))

		if not self.reflected_or_rotated:
			self.med_bucket = self.median_group(group_bucket)
		else:
			self.reflected_or_rotated=False
		
	def letters(self):	
		group_letters=[]
		#K
		for i in range(0,16):
			group_letters.append(self.create_l(self.letters_list[i],self.letters_list[i+1],color="black",width=6))
		
		#F
		for i in range(17,32):
			group_letters.append(self.create_l(self.letters_list[i],self.letters_list[i+1],color="black",width=6))
		group_letters.append(self.create_l(self.letters_list[32],self.letters_list[17],color="black",width=6))
		#C
		for i in range(34,47):
				group_letters.append(self.create_l(self.letters_list[i],self.letters_list[i+1],color="black",width=6))
		group_letters.append(self.create_l(self.letters_list[47],self.letters_list[34],color="black",width=6))
		
		
		if not self.reflected_or_rotated:
			self.med_letters = self.median_group(group_letters)
		else:
			self.reflected_or_rotated=False

	def update_lagrima(self):
		self.lagrima_list = [self.coronel_sanders_list[85],	[self.coronel_sanders_list[85][0]+3,self.coronel_sanders_list[85][1]+5]]
		
	def lagrima(self):
		group_lagrima = []
		
		group_lagrima.append(self.create_l(self.lagrima_list[0],self.lagrima_list[1],color="blue",width=8))

		if not self.reflected_or_rotated:
			self.med_lagrima = self.median_group(group_lagrima)
		else:
			self.reflected_or_rotated=False		

	def coronel_sanders(self):
		group_coronel_sanders = []	
		for i in range(0,55):
			group_coronel_sanders.append(self.create_l(self.coronel_sanders_list[i],self.coronel_sanders_list[i+1],color="black",width=8))
		group_coronel_sanders.append(self.create_l(self.coronel_sanders_list[55],self.coronel_sanders_list[0],color="black",width=8))

		for i in range(56,70):
			 group_coronel_sanders.append(self.create_l(self.coronel_sanders_list[i],self.coronel_sanders_list[i+1],color="black",width=8))

		for i in range(71,84):
			 group_coronel_sanders.append(self.create_l(self.coronel_sanders_list[i],self.coronel_sanders_list[i+1],color="black",width=8))

		for i in range(85,103):
			 group_coronel_sanders.append(self.create_l(self.coronel_sanders_list[i],self.coronel_sanders_list[i+1],color="black",width=8))

		
		#print(self.coronel_sanders_list[85],self.coronel_sanders_list[103])

		if not self.reflected_or_rotated:
			self.med_coronel_sanders = self.median_group(group_coronel_sanders)
		else:
			self.reflected_or_rotated=False		
	def animation(self):
		#self.bucket()
		#self.letters()
		#self.coronel_sanders()
		#self.chicken1()
		
		#self.bucket_list,self.med_bucket = self.escale(self.bucket_list,self.med_bucket,0.8,0.8)
		#self.letters_list,self.med_letters = self.escale(self.letters_list,self.med_letters,0.8,0.8)
		#self.coronel_sanders_list,self.med_coronel_sanders = self.escale(self.coronel_sanders_list,self.med_coronel_sanders,0.8,0.8)
		#self.chicken_1_list,self.med_chicken = self.escale(self.chicken_1_list,self.med_chicken_1,0.8,0.8)

		#print(self.all_points)
		
		self.all_points = self.escale(self.all_points,self.med_all,0.875,0.875)
		self.all_points=self.translate(self.all_points,800,0)
		self.all_points = self.shearing(self.all_points,self.med_all,-0.2,0)
		
		pygame.mixer.music.load("carspeed.wav") #yelling
		pygame.mixer.music.play()

		for i in range(0,8):
			time.sleep(0.01)
			self.all_points = self.escale(self.all_points,self.med_all,1.02,1.02)
			self.all_points=self.translate(self.all_points,-100,0)
			#self.all_points = self.shearing(self.all_points,self.med_all,0.025,0)
			self.all_groups()
			self.canvas1.update()

		pygame.mixer.music.stop()
		self.all_points = self.shearing(self.all_points,self.med_all,0.2,0)
		self.all_groups()
		

		self.canvas1.update()

		pygame.mixer.music.load("bounce.wav") 
		pygame.mixer.music.play()
		time.sleep(0.1)
		self.all_points = self.rotate(self.all_points,self.med_all,-20)	
		self.all_groups()
		self.canvas1.update()
		pygame.mixer.music.stop()
		time.sleep(0.2)
		pygame.mixer.music.load("bounce.wav") 
		pygame.mixer.music.play()
		self.all_points = self.rotate(self.all_points,self.med_all, 20)	
		self.all_groups()
		self.canvas1.update()
		pygame.mixer.music.stop()
		time.sleep(0.2)
		pygame.mixer.music.load("bounce.wav") 
		pygame.mixer.music.play()
		self.all_points = self.rotate(self.all_points,self.med_all, 40)	
		self.all_groups()
		pygame.mixer.music.stop()
		self.canvas1.update()
		time.sleep(0.2)
		pygame.mixer.music.load("bounce.wav") 
		pygame.mixer.music.play()
		self.all_points = self.rotate(self.all_points,self.med_all,-60)	
		self.all_groups()
		self.canvas1.update()
		pygame.mixer.music.stop()

		self.all_groups()
		time.sleep(1)

		pygame.mixer.music.load("sad.wav") #crying
		pygame.mixer.music.play()
		#pygame.mixer.music.load("carspeed.wav") #falling
		#pygame.mixer.music.play()
		for i in range(0,4):
			time.sleep(0.01)
			self.all_points = self.rotate(self.all_points,self.med_all,-20)	
			self.all_groups()
			self.canvas1.update()
		#pygame.mixer.music.stop()
		
		pygame.mixer.music.load("jab.wav") #crying
		pygame.mixer.music.play()
		
		self.all_points = self.rotate(self.all_points,self.med_all,-20)	
		self.chicken_1_list.clear()
		
		self.all_groups()
		self.canvas1.update()
		pygame.mixer.music.stop()
		
		pygame.mixer.music.load("sad.wav") #crying
		pygame.mixer.music.play()

		time.sleep(0.6)

		
		
		self.lagrima()
		self.update_lagrima()
		for i in range(0,10):
			time.sleep(0.01)
			self.lagrima_list=self.translate(self.lagrima_list,0,25)
			self.lagrima_list = self.escale(self.lagrima_list,self.med_lagrima,1.002,1.05)
			self.lagrima()
			self.all_groups()
			self.canvas1.update()
		self.lagrima()
		pygame.mixer.music.stop()

		self.canvas1.update()

			#self.bucket_list=self.translate(self.bucket_list,-20)
			#self.shearing(self.bucket_list,0.5,0.1)
			#self.bucket_list=self.rotate(self.bucket_list,45)
			

			#self.letters_list=self.rotate(self.letters_list,45)
			

			#self.coronel_sanders_list=self.rotate(self.coronel_sanders_list,45)
			

			#self.chicken_1_list=self.rotate(self.chicken_1_list,45)
			#self.all_points = self.escale(self.all_points,self.med_all,0.99,0.99)
			#self.bucket_list = self.escale(self.bucket_list,self.med_bucket,0.9,0.9)

			#self.all_points = self.translate(self.all_points,20,0)		
			#self.all_points = self.rotate(self.all_points,self.med_all,10)	
			#self.all_points = self.shearing(self.all_points,self.med_all,0.9,0)
			#self.all_points = self.reflexion(self.all_points,self.med_all,1)
			
			#self.letters()
			#self.coronel_sanders()
			#self.chicken1()
			
				
	
	def median_all_groups(self,g):
		r = []
		
		m = np.amin(g, axis = 0)
		mm = np.amax(g, axis = 0)
		m_x = int(m[0])
		m_y = int(m[1])
		mm_x = int(mm[0])
		mm_y = int(mm[1])
		
		
		return [(mm[0]+m[0])/2,(mm[1]+m[1])/2]
	
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

	

	def create_l(self,p1,p2, color="lightgray",width=3):
		self.L=[]
		self.bresenham_real_mod(p1,p2)
		for p in self.L:
			self.canvas1.create_line(p[0],p[1],p[0]+1,p[1],fill=color,width=width)
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
		

	
	def escale(self,group,med_group,sx = 1 , sy = 1):
		self.canvas1.delete(tk.ALL)
	
		coordinate_aux = med_group
		#self.translate(0,0)
		self.L_aux=np.asarray(group)
		
		self.L_aux=np.subtract(self.L_aux,med_group)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1 = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
		self.L_aux = aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.add(self.L_aux,med_group)
		group = np.array(self.L_aux).tolist()
		
		return group
		#self.translate(coordinate_aux[0],coordinate_aux[1])
		
		

	def rotate(self,group,med_group,alpha = 45):
		self.canvas1.delete(tk.ALL)
				
		med_group[1] = deepcopy(self.change_origin(med_group[1]))

		coordinate_aux = med_group
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,med_group)

		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))

		cos_alpha = math.cos(math.radians(alpha))
		sen_alpha = math.sin(math.radians(alpha))
		aux1=np.array([[cos_alpha,sen_alpha,0],[-sen_alpha,cos_alpha,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,med_group)

		med_group[1] = deepcopy(self.change_origin(med_group[1]))

		group= np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.reflected_or_rotated = True
		#self.translation(coordinate_aux[0],coordinate_aux[1])
		return group

	def shearing(self, group,med_group ,cx = 0 ,cy = 0):
		self.canvas1.delete(tk.ALL)
		
		med_group[1] = deepcopy(self.change_origin(med_group[1]))
		coordinate_aux = med_group
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,med_group)


		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,cx,0],[cy,1,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		
		self.L_aux=np.add(self.L_aux,med_group)
		med_group[1] = deepcopy(self.change_origin(med_group[1]))
		group = np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		return group

	def reflexion(self,group,med_group ,reflexion_type = 1,rotate_degrees = None):
		
		#reflexion_type = 1 then reflect x, 2 reflect y , 3 reflect on degree line, that pass through origin
		self.canvas1.delete(tk.ALL)
		
		if reflexion_type == 3:
			self.rotate(rotate_degrees)

		med_group[1] = deepcopy(self.change_origin(med_group[1]))
		
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		self.L_aux=np.asarray(group)
		self.L_aux=np.subtract(self.L_aux,med_group)

		
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		
		if reflexion_type == 1 or reflexion_type == 3:
			aux1=np.array([[1,0,0],[0,-1,0],[0,0,1]])
		elif reflexion_type == 2:
			aux1=np.array([[-1,0,0],[0,1,0],[0,0,1]])	
	
			
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		

		self.L_aux=np.add(self.L_aux,med_group)
		med_group[1] = deepcopy(self.change_origin(med_group[1]))
		
		group = np.array(self.L_aux).tolist()
		for i in range(len(group)):
			group[i][1] = self.change_origin(group[i][1])
		
		if reflexion_type == 3 != 0:
			self.rotate(-rotate_degrees)
			self.reflected_or_rotated = True
		
		return group
		

aplicacion1=Aplicacion()