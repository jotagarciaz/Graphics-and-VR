# IFS fractals
# FB - 201003221
from PIL import Image
import random

### Fractint IFS definition of Fern
##self.mat=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
##     [0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
##     [0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
##     [-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]

### Fractint IFS definition of Dragon
##self.mat = [[0.824074, 0.281482, -0.212346,  0.864198, -1.882290, -0.110607, 0.787473],
##       [0.088272, 0.520988, -0.463889, -0.377778,  0.785360,  8.095795, 0.212527]]

### Levy C curve
#self.mat = [[0.5, -0.5, 0.5, 0.5, 0.0, 0.0, 0.5],
#      [0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5]]

# Levy Dragon
#self.mat = [[0.5, -0.5, 0.5, 0.5, 0.0, 0.0, 0.5],
#       [-0.5, -0.5, 0.5, -0.5, 1.0, 0.0, 0.5]]
# Sierpinski
#self.mat = [[0.5, 0, 0, 0.5, 1, 1, 0.33], [0.5, 0, 0, 0.5, -1, 1, 0.33], [0.5, 0, 0, 0.5, 0, -1, 0.33]]
#self.mat = 

class IFS:
	def __init__(self):
		self.mat = [[0,0.08,-0.24,0,-4.5,6.1,0.03225806452], #J Vertical
		[0.1,0,0,0.1,-6,8,0.03225806452], #J Arriba
		[0.08,0,0,0.1,-6,-0.8,0.03225806452], # J Abajo

[0.1,0,0,0.1,-2,8,0.03225806452], #G Arriba
[0,0.08,-0.24,0,-2.6,6.1,0.03225806452], #G Vertical Izquierda
[0.1,0,0,0.1,-2,-0.8,0.03225806452],	#G Abajo
[0, 0.06, -0.1, 0, -0.1, 2.6, 0.03225806452], #G Vertical Derecha
[0.06, 0, 0, 0.06, -1, 3.5, 0.03225806452],# G Vertical Centro


[0,0.08,-0.28,0,1.4,6,0.03225806452], # A VI
[0.1, 0, 0, 0.1, 2, 8, 0.03225806452], # A Arriba
[0,0.08,-0.28,0,3.8,6,0.03225806452], # A VD
[0.05, 0, 0, 0.06, 2.5, 3.6, 0.03225806452], # A Centro

[0,0.08,-0.28,0,5.4,6.0,0.03225806452],#R vertical grande
[0.1,0,0,0.1,6,8,0.03225806452],#R arriba
[0,0.08,-0.16,0,8,7.0,0.03225806452],#R vertical peque
[0.06, 0, 0, 0.06, 6.5, 3.6, 0.03225806452],#R centro
[0.065,0.05,-0.12,0.065,6.8,2,0.03225806452],#R con angulo

[0.1, 0, 0, 0.1, 10, -0.8, 0.03225806452],#C abajo
[0.1, 0, 0, 0.1, 10, 8, 0.03225806452],#C arriba
[0,0.08,-0.24,0,9.4,6.1,0.03225806452],#C vertical arriba


[0,0.08,-0.24,0,14.5,6.1,0.03225806452],#I
[0.1, 0, 0, 0.1, 14, -0.8, 0.03225806452],#I
[0.1, 0, 0, 0.1, 14, 8, 0.03225806452],#I


[0,0.08,-0.28,0,17.4,6,0.03225806452], # A VI
[0.1, 0, 0, 0.1, 18, 8, 0.03225806452], # A Arriba
[0,0.08,-0.28,0,19.8,6,0.03225806452], # A VD
[0.05, 0, 0, 0.06, 18.5, 3.6, 0.03225806452], # A Centro


[0.1, 0, 0, 0.1,22, -0.8, 0.03225806452],#Z abajo
[0.1, 0, 0, 0.1, 22, 8, 0.03225806452],#Z arriba

[-0.065,0.05,-0.2,-0.06,23.5,6.1,0.03225806452],#Z vertical 

] #S

	def inserta_ifs(self,a,b,c,d,e,f,p):
		self.mat.append([a,b,c,d,e,f,p])
	
	def genera_ifs(self):
		# image size
		imgx = 2600
		imgy = 800 # will be auto-re-adjusted
		
		m = len(self.mat)
		# find the xmin, xmax, ymin, ymax
		x = self.mat[0][4]
		y = self.mat[0][5]
		#
		xa = x
		xb = x
		ya = y
		yb = y
		#
		for k in range(imgx * imgy):
			p=random.random()
			psum = 0.0
			for i in range(m):
				psum += self.mat[i][6]
				if p <= psum:
					break
			x0 = x * self.mat[i][0] + y * self.mat[i][1] + self.mat[i][4]
			y  = x * self.mat[i][2] + y * self.mat[i][3] + self.mat[i][5]
			x = x0
			#
			if x < xa:
				xa = x
			if x > xb:
				xb = x
			if y < ya:
				ya = y
			if y > yb:
				yb = y
		
		# drawing
		imgy = round(imgy * (yb - ya) / (xb - xa)) # auto-re-adjust the aspect ratio
		image = Image.new("L", (imgx,imgy))
		
		x=0.0
		y=0.0
		for k in range(imgx * imgy):
			p=random.random()
			psum = 0.0
			for i in range(m):
				psum += self.mat[i][6]
				if p <= psum:
					break
			x0 = x * self.mat[i][0] + y * self.mat[i][1] + self.mat[i][4]
			y  = x * self.mat[i][2] + y * self.mat[i][3] + self.mat[i][5]
			x = x0
			jx = int((x - xa) / (xb - xa) * (imgx - 1))
			jy = (imgy - 1) - int((y - ya) / (yb - ya) * (imgy - 1))
			image.putpixel((jx, jy), 250)
		
		image.save("IFS.png")
		image.show()

if __name__ == "__main__":
	ifs = IFS()
	#ifs.inserta_ifs()
	ifs.genera_ifs()