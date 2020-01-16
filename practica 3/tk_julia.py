# Mandelbrot Fractal using Tkinter
# FB36 - 20130706

#
import tkinter
from tkinter import *
import numpy as np
WIDTH = 640; HEIGHT = 480
xa = -2.0; xb = 1.0
ya = -1.5; yb = 1.5
maxIt = 256

creal = 0.86
cimaginary = -0.223

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

real = np.linspace(-1.5, 1.5, WIDTH)
imaginary = np.linspace(-1.0, 1.0, HEIGHT)

for ky in range(HEIGHT): #si haces hilos de Ky, cada hilo hace kx, lo que lo optimiza bastante
    for kx in range(WIDTH):
        c = complex(creal, cimaginary)
        z = complex(real[kx], imaginary[ky])
        for i in range(maxIt):
            if abs(z) >= 2.0:
                break
            z = z * z + c
        rd = hex(i % 4 * 64)[2:].zfill(2)
        gr = hex(i % 8 * 32)[2:].zfill(2)
        bl = hex(i % 16 * 16)[2:].zfill(2)
        img.put("#" + rd + gr + bl, (kx, ky))

canvas.pack()
mainloop()