#!/usr/bin/python3
from vpython import *

size = 1 #ballSize
m = 1 #kg
v = 100 #m/s
h = 100 #m

L = 100
b = 1 #drag
g = 9.8 #m/s^2
t = 0
dt = 0.01

scene = canvas(title="ExtraCredit",width=1200,height=800,x=0,y=0,center=vector(0,h/2,0),background=vector(0,0.6,0.6))

floor = box(pos=vector(0,-size,0),length=L,width=30,height=0.01,texture=textures.wood)

gd1 = graph(title="x-t plot",width=800,height=600,x=0,y=800,xtitle="t(s)",ytitle="x(m)")
gd2 = graph(title="h-t plot",width=800,height=600,x=0,y=1400,xtitle="t(s)",ytitle="h(m)")
gd3 = graph(title="v-t plot",width=800,height=600,x=0,y=2000,xtitle="t(s)",ytitle="v(m/s)")

xt = gcurve(graph=gd1,color=color.red)
ht = gcurve(graph=gd2,color=color.red)
vt = gcurve(graph=gd3,color=color.red)

#Main
ball = sphere(radius=size,pos=vector(-L/2,h,0),texture=textures.metal,make_trail=True)
ball.v = vector(v,0,0)
ball.a = vector(0,-g,0)

while ball.pos.y >= 0:
    rate(100)
    f = ball.v*(-b)
    ball.a = vector(0,-g,0) + f/m
    ball.v += (ball.a)*dt
    ball.pos += (ball.v)*dt
    ball_v = (ball.v.x**2+ball.v.y**2)**0.5
    ball_x = ball.pos.x + (L/2)
    xt.plot(pos=(t,ball_x))
    ht.plot(pos=(t,ball.pos.y))
    vt.plot(pos=(t,ball_v))
    t += dt

print("finish")
