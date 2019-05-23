# One-dimentional motion simulation (constant speed)
from vpython import *

#variables
size = 0.1#length of cube
L = 1     #length of floor
v = 0.03  #speed of cube
t = 0     #time
dt = 0.01 #time interval

#screen setting
    #the stuff in the simulation
scene = canvas(title="1D Motion",width=800,height=600,x=0,y=0,center=vector(0,0.1,0),background=vector(0,0.6,0.6))
floor = box(pos=vector(0,0,0),length=L,width=L*0.5,height=size*0.1,color=color.blue)
cube = box(pos=vector(-L*0.5+size*0.5,size*0.55,0),length=size,width=size,height=size,color=color.red)
cube.v = vector(v,0,0)
    #the graph and diagram
gd = graph(title="x-t plot",width=800,height=600,x=0,y=600,xtitle="t(s)",ytitle="x(m)")
gd2 = graph(title="v-t plot",width=800,height=600,x=0,y=1200,xtitle="t(s)",ytitle="v(m/s)")
xt = gcurve(graph=gd,color=color.red)
vt = gcurve(graph=gd2,color=color.red)

#Main
while(cube.pos.x <= L*0.5 - size*0.5):
    rate(1000)
    cube.pos.x += v*dt
    xt.plot(pos = (t, cube.pos.x))
    vt.plot(pos = (t, cube.v.x))
    t += dt
print("t = "+str(t))
