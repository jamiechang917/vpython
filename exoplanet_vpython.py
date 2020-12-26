from vpython import *
import numpy as np

dt = 60 #s
t_max = 86400*30 #s
t_steps = int(t_max/dt)
t = 0

G = np.float(6.67*(10**-11))
AU = np.float(1.495978707E11) #m
R_sun = np.float(1.116*696340000) #m
R_planet = np.float(1.44*69911000) #m
M_sun = np.float(1.078*1.989E30) #kg
M_planet = np.float(0.917*1.898E27) #kg

ecc = 0.07
a = 0.04016 * AU


def instant_speed(r):
    return np.float((G*M_sun*((2/abs(r))-(1/a)))**0.5)

P0_planet = vector(-a*(1+ecc)/2,0,0)
P0_sun = vector(0,0,0)

V0_planet = vector(0,-instant_speed(P0_planet.x),0)
V0_sun = vector(0,0,0)

scene = canvas(title="CoRoT-12b Simulation",width=800,height=600,x=0,y=0,center=vector(0,0,0),background=vector(0,0.6,0.6))
scene.lights = []
sunlight = local_light(pos=P0_sun,color=color.yellow)


sun = sphere(radius=R_sun,pos=P0_sun,make_trail=True,emissive=True,texture="https://i.imgur.com/XdRTvzj.jpeg",flipx = False , shininess = 0.9)
planet = sphere(radius=R_planet,pos=P0_planet,make_trail=False,retain=50,texture="https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",opacity = 0.7)

sun.v = V0_sun
planet.v = V0_planet


def g_f():
    r = sun.pos - planet.pos
    g_f = r*(G/(mag(r)**3))
    return g_f


# gd = graph(title="h-t plot",width=800,height=600,x=0,y=600,xtitle="t(s)",ytitle="h(m)")
# gd2 = graph(title="vertical v-t plot",width=800,height=600,x=0,y=1200,xtitle="t(s)",ytitle="v(m/s)")
# gd3 = graph(title="horizontal distance plot",width=800,height=600,x=0,y=1800,xtitle="t(s)",ytitle="x(m)")

# ht = gcurve(graph=gd,color=color.red)
# vt = gcurve(graph=gd2,color=color.red)
# xt = gcurve(graph=gd3,color=color.red)

while t<t_max:
    rate(50)
    #sun.a = -g_f()*M_planet
    planet.a = g_f()*M_sun
    #sun.v += sun.a*dt
    planet.v += planet.a*dt
    #sun.pos += sun.v*dt
    planet.pos += planet.v*dt
    t += dt

