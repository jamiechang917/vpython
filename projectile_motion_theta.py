from vpython import *
import random

size = 1
m = 1
v = 120
h = 0
theta = radians(15) # radians(angle)
L = 300
b = 0.5 # f = -b*v
g = 9.8
t = 0
dt = 0.01

max_horizontal_dispersion = 10
max_vertical_dispersion = 10
sigma = 1.8 #(1.0~3.0)


scene = canvas(title="projectile_motion_theta",width=1200,height=600,x=0,y=0,center=vector(0,h/2,0),background=vector(0,0.6,0.6))
floor = box(pos=vector(0,-size,0),length=L,width=30,height=0.01,texture=textures.wood)

gd1 = graph(title="x-t plot",width=800,height=600,x=0,y=600,xtitle="t(s)",ytitle="x(m)")
gd2 = graph(title="h-t plot",width=800,height=600,x=0,y=1200,xtitle="t(s)",ytitle="h(m)")
gd3 = graph(title="v-t plot",width=800,height=600,x=0,y=1800,xtitle="t(s)",ytitle="v(m/s)")

xt = gcurve(graph=gd1,color=color.red)
ht = gcurve(graph=gd2,color=color.red)
vt = gcurve(graph=gd3,color=color.red)

#Main

for i in range(12):
	ball = sphere(radius=size,pos=vector(-L/2,h,0),texture=textures.metal,make_trail=True)
	ball.v = vector(v*cos(theta),v*sin(theta),0)
	ball.a = vector(0,-g,0)

	rng = random.uniform(0.5,1)
	sigma_use = random.uniform(1.0,sigma)
	positive_or_negative = 0
	positive_or_negative_rng = random.randint(0,1)
	
	if positive_or_negative_rng == 0:
		positive_or_negative = -1
	elif positive_or_negative_rng == 1:
		positive_or_negative_rng = 1
	if sigma_use >= 1.5:
		max_horizontal_dispersion = positive_or_negative * (max_horizontal_dispersion/sigma) *rng
		max_vertical_dispersion = positive_or_negative * (max_vertical_dispersion/sigma) *rng
	elif sigma_use < 1.5:
		max_horizontal_dispersion = (max_horizontal_dispersion) *rng
		max_vertical_dispersion = (max_vertical_dispersion) *rng
	ball.v.x += (max_vertical_dispersion/10)
	ball.v.z += (max_horizontal_dispersion/10)		

	while ball.pos.y >=0:
		rate(100)
		f = ball.v * (-b)
		ball.a = vector(0,-g,0) + f/m
		ball.v += (ball.a)*dt
		ball.pos += (ball.v)*dt
		ball_v = (ball.v.x**2+ball.v.y**2)**0.5
		xt.plot(pos=(t,ball.pos.x))
		ht.plot(pos=(t,ball.pos.y))
		vt.plot(pos=(t,ball_v))
		t += dt

	print("t = "+str(t)+" , x = "+str(ball.pos.x+L/2))

	
