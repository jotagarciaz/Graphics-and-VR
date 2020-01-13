"""
@author: Joaquín García Benítez
@brief: First assignment for Computer Graphics of the University of Cantabria. We should present a GUI that allows us to draw lines
with different lines algorithms:
	- Slope of the line.
	- D.D.A.
	- Bresenham



"""
import arcade
import os
import copy
import numpy as np
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "transformation 2D algorithms"


class TextButton:
	""" Text-based button """

	def __init__(self,
				 center_x, center_y,
				 width, height,
				 text,
				 font_size=18,
				 font_face="Arial",
				 face_color=arcade.color.LIGHT_GRAY,
				 highlight_color=arcade.color.WHITE,
				 shadow_color=arcade.color.GRAY,
				 button_height=1,
				 action_function=None
				 ):
		self.center_x = center_x
		self.center_y = center_y
		self.width = width
		self.height = height
		self.text = text
		self.font_size = font_size
		self.font_face = font_face
		self.pressed = False
		self.face_color = face_color
		self.highlight_color = highlight_color
		self.shadow_color = shadow_color
		self.button_height = button_height
		self.action_function = action_function

	def draw(self):
		""" Draw the button """
		arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
									 self.height, self.face_color)

		if not self.pressed:
			color = self.shadow_color
		else:
			color = self.highlight_color

		# Bottom horizontal
		arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
						 self.center_x + self.width / 2, self.center_y - self.height / 2,
						 color, self.button_height)

		# Right vertical
		arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
						 self.center_x + self.width / 2, self.center_y + self.height / 2,
						 color, self.button_height)

		if not self.pressed:
			color = self.highlight_color
		else:
			color = self.shadow_color

		# Top horizontal
		arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
						 self.center_x + self.width / 2, self.center_y + self.height / 2,
						 color, self.button_height)

		# Left vertical
		arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
						 self.center_x - self.width / 2, self.center_y + self.height / 2,
						 color, self.button_height)

		x = self.center_x
		y = self.center_y
		if not self.pressed:
			x -= self.button_height
			y += self.button_height

		arcade.draw_text(self.text, x, y,
						 arcade.color.WHITE_SMOKE, font_size=self.font_size,
						 width=self.width, align="center",
						 anchor_x="center", anchor_y="center",bold=True
						 )

	def click_area(self, x, y):

		if x < self.center_x + self.width / 2 and x > self.center_x - self.width / 2 and \
				y < self.center_y + self.height / 2 and y > self.center_y - self.height / 2:
			return True
		return False

	def on_press(self):
		self.pressed = True

	def on_release(self):
		self.pressed = False


class LineButton(TextButton):
	def __init__(self,
				 center_x, center_y,
				 width, height,
				 text,
				 font_size=18,
				 font_face="Arial",
				 face_color=arcade.color.CHARCOAL,
				 highlight_color=arcade.color.WHITE,
				 shadow_color=arcade.color.GRAY,
				 button_height=1,
				 action_function=None           
				 ):
		super().__init__(center_x, center_y, width, height, text, font_size, font_face,
			  face_color, highlight_color, shadow_color, button_height, action_function)


def check_buttons_click_area(x, y, button_list):
	""" Given an x, y, see if we need to register any button clicks. """
	for button in button_list:
		if button.click_area(x, y):
			return True
	return False


def check_mouse_press_for_buttons(x, y, button_list):
	""" Given an x, y, see if we need to register any button clicks. """
	for button in button_list:
		if button.click_area(x, y) and not button.pressed:
			button.on_press()
		elif button.click_area(x, y) and button.pressed:
			button.on_release()
		elif button.pressed and check_buttons_click_area(x, y, button_list):
			button.on_release()



class Canvas(arcade.Window):
	"""
	Main application class.

	NOTE: Go ahead and delete the methods you don't need.
	If you do need a method, delete the 'pass' and replace it
	with your own code. Don't leave 'pass' in this program.
	"""

	def __init__(self, width, height, title):
		super().__init__(width, height, title, resizable=True)
		arcade.set_background_color(arcade.color.WHITE_SMOKE)
		self.line_buttons = None
		self.transformation_buttons = None
		self.L = None
		self.first_time_drawing = True
		self.illegal_action= False
		self.Draw = None
		self.med = None
		# If you have sprite lists, you should create them here,
		# and set them to None

	def on_resize(self, width, height):
		""" This method is automatically called when the window is resized. """

		# Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
		# edges being -1 to 1.
		super().on_resize(width, height)

	def setup(self):
		# Create your sprites and sprite lists here
		self.med = []
		self.line_buttons = []
		self.transformation_buttons = []
		self.L = []
		self.Draw = []
		self.L_aux = []
		self.line_buttons.append(LineButton(
			self.width-60, self.height-30, 120, 25, "Slope", 14, "Arial", action_function=self.slope_line))
		self.line_buttons.append(LineButton(
			self.width-200, self.height-30, 120, 25, "Slope Mod.", 14, "Arial", action_function=self.slope_line_mod))
		self.line_buttons.append(LineButton(
			self.width-60, self.height-70, 120, 25, "D.D.A.", 14, "Arial", action_function=self.digital_differential_analyzer))
		self.line_buttons.append(LineButton(self.width-60, self.height-110, 120, 25, "Bresenham I.", 14, "Arial", action_function=self.bresenham))
		self.line_buttons.append(LineButton(self.width-200, self.height-110, 120, 25, "Bresenham I. Mod.", 14, "Arial", action_function=self.bresenham_mod))
		self.line_buttons.append(LineButton(self.width-60, self.height-150, 120, 25, "Bresenham R.", 14, "Arial", action_function=self.bresenham_real))
		self.line_buttons.append(LineButton(self.width-200, self.height-150, 120, 25, "Bresenham R. Mod.", 14, "Arial", action_function=self.bresenham_real_mod))
		
		self.transformation_buttons.append(LineButton(70, self.height-30, 120, 25, "Translation.", 14, "Arial", action_function=self.translation))
	
	def on_draw(self):
		"""
		Render the screen.
		"""

		# This command should happen before we start drawing. It will clear
		# the screen to the background color, and erase what we drew last frame.
		arcade.start_render()

		for button in self.line_buttons:
			button.draw()

		for button in self.transformation_buttons:
			button.draw()

		if self.first_time_drawing:
			arcade.draw_text("Select a button",self.width/2,self.height-300 ,
							arcade.color.COAL, font_size=40,
							width=500, align="center",
							anchor_x="center", anchor_y="center",bold=True
							)

			arcade.draw_text("then click somewhere in the screen",self.width/2,self.height-350 ,
							arcade.color.COAL, font_size=40,
							width=800, align="center",
							anchor_x="center", anchor_y="center",bold=True
					
							)
		
		if self.illegal_action:
			 arcade.draw_text("You're not allowed to do that.",self.width/2,self.height-350 ,
							arcade.color.RED_DEVIL, font_size=40,
							width=800, align="center",
							anchor_x="center", anchor_y="center",bold=True
							)
		
		if len(self.med) > 0:
			arcade.draw_point(int(self.med[0]),int(self.med[1]),arcade.color.AIR_FORCE_BLUE,5)
		if len(self.L) > 0:
			arcade.draw_points(self.L, arcade.color.YALE_BLUE, 5)              
		if len(self.Draw) > 0:
			for l in self.Draw:
				arcade.draw_points(l, arcade.color.RED_DEVIL, 5)



		# Call draw() on all your sprite lists below

	

	def on_mouse_motion(self, x, y, delta_x, delta_y):
		"""
		Called whenever the mouse moves.

		Con self.L_aux len 1 puedes hacer que el segundo punto sea el de esta x e y
		"""

	   
		for button in self.line_buttons:
			if button.pressed:
				if len(self.L_aux) == 1:
					if check_buttons_click_area(x, y, self.line_buttons) == False:
						# si se han introducido dos puntos con un botón pulsado
						self.illegal_action=False

						button.action_function(self.L_aux[0][0], self.L_aux[0][1],  x, y)
					else:
						self.illegal_action = True
						self.L.clear()

	
	def translation(self,x,y,media_group = None): 
		#(0,0) -> (media_group)
		if media_group is not None:
			x, y = x - self.L_aux[0][0] + media_group[0], y - self.L_aux[0][1] + media_group[1]
		else:
			x = x - self.L_aux[0][0]
			y = y - self.L_aux[0][1]

		self.L_aux=np.asarray(self.L_aux)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,0,x],[0,1,y],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.array(self.L_aux).tolist() 
		

	def escale(self,sx,sy,media_group):
	
		coordinate_aux = self.L_aux[0]
		self.translation(0,0,media_group)

		self.L_aux=np.asarray(self.L_aux)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1 = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
		self.L_aux = aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux = np.array(self.L_aux).tolist()

		self.translation(coordinate_aux[0]+sx*(coordinate_aux[0]-media_group[0]),coordinate_aux[1]+sy*(coordinate_aux[1]-media_group[1]),media_group)

	def rotate(self, alpha,media_group):
		coordinate_aux = self.L_aux[0]

		self.translation(0,0,media_group)
		
		self.L_aux=np.asarray(self.L_aux)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))

		cos_alpha = math.cos(math.radians(alpha))
		sen_alpha = math.sin(math.radians(alpha))
		aux1=np.array([[cos_alpha,sen_alpha,0],[-sen_alpha,cos_alpha,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.array(self.L_aux).tolist()
		self.translation(coordinate_aux[0],coordinate_aux[1],media_group)

	def shearing(self,cx,cy):
		coordinate_aux = self.L_aux[0]
		#self.translation(0,0)
		self.L_aux=np.asarray(self.L_aux)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		aux1=np.array([[1,cx,0],[cy,1,0],[0,0,1]])
		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.array(self.L_aux).tolist()
		#self.translation(coordinate_aux[0],coordinate_aux[1])

	def reflexion(self,reflect_x_or_y,media_group):
		#reflect_x_or_y = true then refleclt x else reflect y
		coordinate_aux = self.L_aux[0]

		#self.translation(0,0)

		self.L_aux=np.asarray(self.L_aux)
		m  = self.L_aux.shape
		aux = np.ones((m[0],1))
		aux = np.hstack((self.L_aux,aux))
		if reflect_x_or_y:
			aux1=np.array([[1,0,0],[0,-1,0],[0,0,1]])
		else:
			aux1=np.array([[-1,0,0],[0,1,0],[0,0,1]])

		self.L_aux=aux1.dot(np.transpose(aux))
		self.L_aux = np.transpose(np.delete(self.L_aux,2,0))
		self.L_aux=np.array(self.L_aux).tolist()
		#self.translation(coordinate_aux[0],coordinate_aux[1])

	def slope_line(self, x1, y1, x2, y2):
		self.L.clear()
		x, y = x1, y1
		dx, dy = x2 - x1, y2 - y1
		m = dy/dx
		b = y1 - m * x1
		while x <= x2:
			self.L.append([x, y])
			x = x + 1
			y = round(m*x + b)



	def slope_line_mod(self, x1, y1, x2, y2):
		self.L.clear()
		
		if x2<x1:
			x1, x2 = x2, x1
			y1, y2 = y2, y1

		
		dx, dy = x2 - x1, y2 - y1
		x, y = x1, y1

		if y1 == y2:
			while x <= x2:
				self.L.append([x, y])
				x = x + 1
		elif x1 == x2:
			if y>y2:
				y,y2=y2,y
			while y <= y2:
				self.L.append([x, y])
				y = y + 1
	   
		else:
			m = dy/dx
			if m > 1 :
				m = 1/m
				b = x1 - m*y1
				while y <= y2:
					self.L.append([x, y])
					y = y + 1
					x = round(m*y + b)
			elif m < -1:
				m = abs(1/m)
				b = x1 - m*y1
				y_aux = y
				while y >= y2:
					self.L.append([x, y])
					y = y - 1
					y_aux = y_aux + 1
					x = round(m*y_aux + b)
			else:

				b = y1 - m*x1
				while x <= x2:
					self.L.append([x, y])
					x = x + 1
					y = round(m*x + b)


	
	def bresenham(self, x1, y1, x2, y2):
		self.L.clear()
		x = x1
		y = y1
		dx = x2 - x1
		dy = y2 - y1
		ne = 2*dy - dx
		for _ in range(0, dx+1):
			self.L.append([x,y])
			while ne > 0:
				y = y + 1
				ne = ne - 2*dx
			x = x + 1
			ne = ne + 2*dy
		   
		

	def bresenham_mod(self, x1, y1, x2, y2):
		self.L.clear()
		x = x1
		y = y1
		dx = x2 - x1
		dy = y2 - y1
		aux_dx , dx= dx , abs(dx)
		aux_dy , dy= dy , abs(dy)

		
		if dx == 0 or dy>dx:
			ne = 2*dx - dy
			for _ in range(0, dy+1):
				self.L.append([x,y])
				while ne > 0:
					x = x + 1
					ne = ne - 2*dy
				y = y + 1
				ne = ne + 2*dx
		else:
			ne = 2*dy - dx
			for _ in range(0, dx+1):
				self.L.append([x,y])
				while ne > 0:
					y = y + 1
					ne = ne - 2*dx
				x = x + 1
				ne = ne + 2*dy
		
		self.L=np.asarray(self.L)
		self.transform_quadrant(aux_dx, aux_dy)

		if self.L[0][0]<0:
			x1=2*x1
			self.L[...,0] +=x1
		if self.L[0][1]<0:
			y1=2*y1
			self.L[...,1] +=y1
		self.L=np.array(self.L).tolist()        


	def bresenham_real(self, x1, y1, x2, y2):
		self.L.clear()
		x = x1
		y = y1
		dx = x2 - x1
		dy = y2 - y1
		m = dy/dx
		e = m - 1/2
		for _ in range(dx+1):
			self.L.append([x,y])
			while e > 0:
				y = y + 1
				e = e - 1
			x = x + 1
			e = e + m

	
	def bresenham_real_mod(self, x1, y1, x2, y2):
		self.L.clear()
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
		
		

   # Second Line drawer algorithm

	def digital_differential_analyzer(self, x1, y1, x2, y2):
		self.L.clear()
		dx = x2-x1
		dy = y2-y1
		M = max(abs(dx),abs(dy))
		dx_ = dx/M
		dy_ = dy/M
		x = x1+0.5
		y = y1+0.5

		for _ in range(0, M+1):
			self.L.append([x, y])
			x = x+dx_
			y = y+dy_

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
			

	def on_mouse_press(self, x, y, button, key_modifiers):
		"""
		Called when the user presses a mouse button.
		"""
		# En caso de no pinchar en un botón hay posibilidad de estar introduciendo puntos.
		
		check_mouse_press_for_buttons(x, y, self.line_buttons)
		check_mouse_press_for_buttons(x, y, self.transformation_buttons)

		if check_buttons_click_area(x, y, self.line_buttons) == False:
			
			# comprobamos que botón está presionado
			for button in self.line_buttons:
				if button.pressed:
					self.first_time_drawing=False
					self.L_aux.append([x, y])
					self.L.append([x, y])
					# si se han introducido dos puntos con un botón pulsado
					if len(self.L_aux) == 2:
						#self.translation(10,10)
						#self.escale(0.5,0.5)
						#self.rotate(75)
						#self.reflexion(False,media_group)
						
						button.action_function(int(self.L_aux[0][0]),int(self.L_aux[0][1]),int(self.L_aux[1][0]),int(self.L_aux[1][1]))
						self.Draw.append(copy.deepcopy(self.L))
						self.L_aux.clear()
					
					if len(self.Draw) == 3:
						self.Draw_aux = []	
						min = []
						max = []
						while len(self.Draw)>0:
							l = self.Draw.pop()
							self.Draw_aux.append(l)
							min.append(np.amin(l, axis=0))
							max.append(np.amax(l, axis=0))
						min = np.amin(min, axis=0)
						max = np.amax(max, axis=0)
						media_group = np.add(min,max)/2
						

						media_group = self.median_group(self.Draw_aux)
						self.med = media_group
						self.Draw = self.Draw_aux
						
						self.Draw_aux = []	
						while len(self.Draw)>0:
							l = self.Draw.pop()
							self.L_aux = [l[0],l[-1]]
							self.translation(0,0,media_group)
							#self.escale(0.5,0.5,media_group)
							button.action_function(int(self.L_aux[0][0]),int(self.L_aux[0][1]),int(self.L_aux[1][0]),int(self.L_aux[1][1]))
							self.Draw_aux.append(copy.deepcopy(self.L))
						
					
						self.Draw = self.Draw_aux

			
		elif check_buttons_click_area(x, y, self.transformation_buttons) == False:
			for button in self.transformation_buttons:
				if button.pressed:
						button.action_function(20,20)
		else:
			self.L_aux.clear()
	


def main():
	""" Main method """
	canvas = Canvas(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	canvas.setup()
	arcade.run()


if __name__ == "__main__":
	main()