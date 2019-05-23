#terminal speed
from vpython import *

size = 1 #radius
m = 1 #mass(kg)
h = 0 #height
g = 9.8 #9.8 m/s^2
b = 0.3 #airdrag -> F = -bv
t = 0
dt = 0.01

scene = canvas(title="Free Fall",width=800,height=600,x=0,y=0,center=vector(0,h/2,0),background=vector(0,0.6,0.6))
ball = sphere(pos=vector(0,h,0),radius=size,color=color.red)
ball.v = vector(0,0,0)
ball.a = vector(0,-g,0)

gd = graph(title="h-t plot",width=800,height=600,x=0,y=600,xtitle="t(s)",ytitle="h(m)")
gd2 = graph(title="v-t plot",width=800,height=600,x=0,y=1200,xtitle="t(s)",ytitle="v(m/s)")
gd3 = graph(title="a-t plot",width=800,height=600,x=0,y=1800,xtitle="t(s)",ytitle="a(m/s^2)")

ht = gcurve(graph=gd,color=color.red)
vt = gcurve(graph=gd2,color=color.red)
at = gcurve(graph=gd3,color=color.red)

#create a file
file = open("air_drag_vt_data.txt", "w", encoding = "UTF-8")
file.write("t(s), h(m), v(m/s), a(m/s^2)\n")

#Variables for calculating the terminal speed
tp = 0
v2_v1 = 0.00001 #the difference between v2 and v1, when the difference smaller than value(v2_v1),the programming stops.

#Main
while True:
	f = (-b)*(ball.v)#f is positive if the ball is falling down
	v1 = ball.v.y
	ball.a = vector(0,-g,0) + f/m
	ball.v += (ball.a)*dt
	ball.pos += (ball.v)*dt
	ht.plot(pos=(t,ball.pos.y))
	vt.plot(pos=(t,ball.v.y))
	at.plot(pos=(t,ball.a.y))
	v2 = ball.v.y
	#write data to the file in every 0.1 second
	tc = t
	if(tc == 0 or tc-tp >=0.1):
		file.write("t = "+str(t)+","+"position = "+str(ball.pos.y)+","+"speed = "+str(ball.v.y)+","+"acceleration = "+str(ball.a.y)+"\n")
		tp=tc #set tp to t
	#CONTINUE OR STOP
	if (v1 - v2) <= v2_v1: #v1 and v2 are negative,so the difference between them is v1-v2
		t += dt		
		break
	else:
		t += dt

print("t = "+str(t)+" , terminal speed = "+str(ball.v.y))
file.close()
