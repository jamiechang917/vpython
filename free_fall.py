# free fall
from vpython import *

size = 1 #radius of the ball
e = 0.9 #coefficient of restitution
i = 0 #times of collision
N = 50 # limit of the times of collision
h = 20 # the height of ball
g = 19.6 # 9.8m/s^2
t = 0
dt = 0.001

scene = canvas(title="Free Fall",width=800,height=600,x=0,y=0,center=vector(0,h/2,0),background=vector(0,0.6,0.6))
floor = box(pos=vector(0,0,0),length=40,width=10,height=0.01,color=color.blue)
ball = sphere(pos=vector(0,h,0),radius=size,color=color.red)
ball.v = vector(0,0,0)
ball.a = vector(0,-g,0)

gd = graph(title="plot",width=800,height=600,x=0,y=600,xtitle="t(s)",ytitle="blue=h(m),red=v(m/s)")
ht = gcurve(graph=gd,color=color.blue)
vt = gcurve(graph=gd,color=color.red)

#Main
while i < N:
	rate(1000)
	ball.v.y -= g*dt
	ball.pos.y += ball.v.y*dt
	ht.plot(pos=(t,ball.pos.y))
	vt.plot(pos=(t,ball.v.y))
	if ball.pos.y <= size+floor.height/2 and ball.v.y < 0:
		ball.v.y = -ball.v.y*e
		i += 1
	t += dt
print("i = "+str(i))
print("t = "+str(t))
