from vpython import *
import random

# Variables 1:10
size = 1
m = 17.6
v = 98.5
theta = radians(20)
h = 20
g = 9.8
L = 900
b = 0.3
t = 0
dt = 0.01
sigma = 2.0
shells = 100
locked = True

max_horizontal_dispersion = 16.7 #abbreviate of HD (1:10)


sense = canvas(title="gun simulation",width=1200,height=600,x=0,y=0,background=vector(0,0.6,0.6),center=vector(0,h/2,0))
floor = box(pos=vector(0,-size,0,),length=L,width=max_horizontal_dispersion,height=0.01,texture=textures.wood)

if locked ==True:
	max_horizontal_dispersion *= 0.5

#Rng
t_HD = 2*v*sin(theta)/g
speed_to_adjust_for_HD_0 = ((max_horizontal_dispersion*g)/t_HD)/10
speed_to_adjudt_for_VD_0 = v*cos(theta) * 0.03
p = 100 #100%
if sigma <=1.0 and sigma > 0:
	p =22.6
	p -= 11.2*(sigma-0)
	p = 2*((22.6+p)*sigma/2)
elif sigma <= 2.0 and sigma >1.0:
	p =11.4
	p -= 9.3*(sigma-1)
	p = 68 + 2*((11.4+p)*(sigma-1.0)/2)
elif sigma <= 3.0 and sigma > 2.0:
	p = 2.1
	p -= 2.1*(sigma-2)
	p = 95 + 2*((2.1+p)*(sigma-2)/2)


for _ in range(int(shells)):
	t = 0
	speed_to_adjust_for_HD = speed_to_adjust_for_HD_0
	speed_to_adjudt_for_VD = speed_to_adjudt_for_VD_0
	ball = sphere(radius=size,pos=vector(-L/2,h,0),color=color.red)
	ball.v = vector(v*cos(theta),v*sin(theta),0)
	ball.a = vector(0,-g,0)
	#rng
	rng = random.uniform(0.0,1.0)
	rng2 = random.uniform(0.5,1.0)
	rng3 = random.uniform(0.0,1.0)
	rng4 = random.uniform(0.5,1.0)
	dispersion = random.randint(1,100)
	positive_or_negative_h = random.randint(0,1)
	positive_or_negative_v = random.randint(0,1)

	if dispersion < p:
		speed_to_adjust_for_HD *= rng
		speed_to_adjust_for_HD /= (rng2*sigma)
	elif dispersion >= p:
		speed_to_adjust_for_HD *= rng
	if dispersion < p:
		speed_to_adjudt_for_VD *= rng3
		speed_to_adjudt_for_VD /= (rng4*sigma)
	elif dispersion >= p:
		speed_to_adjudt_for_VD *= rng3

	if positive_or_negative_h == 0:
			ball.v.z += speed_to_adjust_for_HD
	elif positive_or_negative_h == 1:
			ball.v.z -= speed_to_adjust_for_HD
	if positive_or_negative_v == 0:
			ball.v.x += speed_to_adjudt_for_VD
	elif positive_or_negative_v == 1:
			ball.v.x -= speed_to_adjudt_for_VD

	while True:
		if ball.pos.y < 0 and ball.v.y <0:
			break
		else:
			rate(2000)
			f = -b*ball.v
			ball.a = vector(0,-g,0) + f/m
			ball.v += ball.a*dt
			ball.pos += ball.v*dt
		t += dt
	print("t = "+str(t)+", ball.pos(x,y,z)"+str(ball.pos))
#standerd
ball = sphere(radius=size,pos=vector(-L/2,h,0),color=color.white,make_trail=True)
ball.v = vector(v*cos(theta),v*sin(theta),0)
ball.a = vector(0,-g,0)
t = 0	
while True:
	if ball.pos.y < 0 and ball.v.y <0:
		break
	else:
		rate(100)
		f = -b*ball.v
		ball.a = vector(0,-g,0) + f/m
		ball.v += ball.a*dt
		ball.pos += ball.v*dt
		scene.center = ball.pos
	t += dt
print("standered: t = "+str(t)+", ball.pos(x,y,z)"+str(ball.pos))
			
