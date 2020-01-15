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
class IFS:
    def __init__(self):
        self.mat = []

    def inserta_ifs(self,a,b,c,d,e,f,p):
        self.mat.append([a,b,c,d,e,f,p])
    
    def genera_ifs(self):
        # image size
        imgx = 1280
        imgy = 720 # will be auto-re-adjusted
        
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
            image.putpixel((jx, jy), 255)
        
        image.save("IFS.png")
        image.show()

if __name__ == "__main__":
    ifs = IFS()
    ifs.inserta_ifs()
    ifs.genera_ifs()