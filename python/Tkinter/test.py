#coding: utf-8
from Tkinter import *
from math import sin, cos, pi
WIDTH = 600
HEIGHT = 600
CENTER = (WIDTH/2,HEIGHT/2)
RADIUS = 150
POLY = 10


FRAMES_PER_SEC = 1


root = Tk()
root.title('clock-computer')
graph = Canvas(root, width=WIDTH, height=HEIGHT, background='white')
graph.create_oval((CENTER[0]-RADIUS, CENTER[1]-RADIUS,CENTER[0]+RADIUS,CENTER[1]+RADIUS),outline='blue',width=2)


TIMER = 0
def update():
	global TIMER
	TIMER = (TIMER+1)%POLY**3
	i,j,k = TIMER%POLY,TIMER/POLY,TIMER/POLY**2
	graph.coords(S,CENTER+ (CENTER[0]+sin(2*pi*i/POLY)*130,CENTER[1]-cos(2*pi*i/POLY)*130))
	graph.coords(M,CENTER+(CENTER[0]+sin(2*pi*j/POLY)*100,CENTER[1]-cos(2*pi*j/POLY)*100))
	graph.coords(H,CENTER+(CENTER[0]+sin(2*pi*k/POLY)*70,CENTER[1]-cos(2*pi*k/POLY)*70))
	graph.after(1000 / FRAMES_PER_SEC, update)


for i in xrange(POLY):
	graph.create_text((CENTER[0]+sin(2*pi*i/POLY)*(RADIUS-10),CENTER[1]-cos(2*pi*i/POLY)*(RADIUS-10)),text=i)
o=graph.create_text(CENTER,text='Lambda')
H=graph.create_line(CENTER+(CENTER[0],CENTER[1]-70),fill='black',width=3)
M=graph.create_line(CENTER+(CENTER[0],CENTER[1]-100),fill='brown',width=2)
S=graph.create_line(CENTER+(CENTER[0],CENTER[1]-130),fill='red',width=1)
graph.after(1000 / FRAMES_PER_SEC, update)
graph.pack()


root.mainloop()
