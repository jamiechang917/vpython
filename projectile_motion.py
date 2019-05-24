#Projectile Motion (including gravity and airdrag)
from vpython import *

L = 100 # the length of floor
size = 1 # the radius of ball
m = 1 # mass of ball (kg)
h = 100 # the height of ball
v = 10 # the initial speed of ball
g = 9.8 #gravity (m/s^2)
b = 0.3 #airdrag coefficient -> f = -b * v
e = 0.9 # coefficient of restitution
i = 0 # the time of collision of the ball
N = 50 # limit of the collision of the ball
t = 0
dt = 0.01

scene = canvas(title="Projectile Motion",width=800,height=600,x=0,y=0,center=vector(0,h/2,0),background=vector(0,0.6,0.6))
floor = box(pos=vector(0,-size,0),length=L,width=10,height=0.001,texture=textures.metal)
ball = sphere(radius=size,pos=vector(-L/2,h,0),texture= textures.wood,make_trail=True)
ball.v = vector(v,0,0)
ball.a = vector(0,-g,0)

gd = graph(title="h-t plot",width=800,height=600,x=0,y=600,xtitle="t(s)",ytitle="h(m)")
gd2 = graph(title="vertical v-t plot",width=800,height=600,x=0,y=1200,xtitle="t(s)",ytitle="v(m/s)")
gd3 = graph(title="horizontal distance plot",width=800,height=600,x=0,y=1800,xtitle="t(s)",ytitle="x(m)")

ht = gcurve(graph=gd,color=color.red)
vt = gcurve(graph=gd2,color=color.red)
xt = gcurve(graph=gd3,color=color.red)

#Main
while True:
    if i < N:
        rate(100)
        ball.v += (ball.a)*dt #gravity force
        ball.v.x += (-b*ball.v.x/m)*dt #airdrag,horizontal
        ball.v.y += (-b*ball.v.y/m)*dt #airdrag,vertical
        ball.pos += (ball.v)*dt
        ht.plot(pos=(t,ball.pos.y))
        vt.plot(pos=(t,ball.v.y))
        xt.plot(pos=(t,ball.pos.x))
    if ball.pos.y <= 0 and ball.v.y < 0:
        ball.v.y = -e*ball.v.y
        i += 1
    elif i >= N:
        break

    t += dt

print("t = "+str(t)+",horizontal distance = "+str(ball.pos.x-(-floor.length/2)))
	
	
	
	
