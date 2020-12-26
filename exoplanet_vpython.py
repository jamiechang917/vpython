
from vpython import *
dt = 60 #s
t = 0

G = 6.67*(10**-11)
AU = 1.495978707E11 #m
R_sun = 1.116*696340000 #m
R_planet = 1.44*69911000 #m
M_sun = 1.078*1.989E30 #kg
M_planet = 0.917*1.898E27 #kg

ecc = 0.07
a = 0.04016 * AU
inclination = (90-85.48) * (pi/180)
w = 105 * (pi/180)

running = False
re = False
end = False

def instant_speed(pos_p,pos_s):
    return (G*M_sun*((2/mag(pos_p-pos_s))-(1/a)))**0.5

# P0_planet = vector(-a*(1-ecc),0,0)
# P0_sun = vector(-ecc*a,0,0)

P0_planet = a*(1-ecc)*vector(sin(w-0.5*pi),cos(w-0.5*pi)*sin(inclination),cos(w-0.5*pi)*cos(inclination))
P0_sun = ecc*a*vector(sin(w-0.5*pi),cos(w-0.5*pi)*sin(inclination),cos(w-0.5*pi)*cos(inclination))

normal_unitvec = vector(0,cos(inclination),-1*sin(inclination))
vel_unitvec = cross(normal_unitvec,P0_planet)/mag(P0_planet)

# V0_planet = vector(0,0,instant_speed(P0_planet,P0_sun))
# V0_sun = vector(0,0,0)

V0_planet = instant_speed(P0_planet,P0_sun)*vel_unitvec
V0_sun = vector(0,0,0)

scene = canvas(title="CoRoT-12b Simulation (Period=2.82d)",width=800,height=600,x=0,y=0,center=vector(0,0,0),background=vector(0,0,0))
scene.lights = []
sunlight = local_light(pos=P0_sun,color=color.yellow)
sun = sphere(radius=R_sun,pos=P0_sun,make_trail=True,emissive=True,texture="https://i.imgur.com/XdRTvzj.jpeg",flipx = False , shininess = 0.9)
planet = sphere(radius=R_planet,pos=P0_planet,make_trail=True,trail_radius=0.1*R_planet,texture="https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",opacity = 0.7)

scene.camera.pos = vector(0,0,0.8*(10**10))
scene_camera_original_pos = scene.camera.pos
scene.camera.center = P0_sun

gd = graph(title="relative flux",width=800,height=600,x=0,y=600,xtitle="Time (Hours)",ytitle="Relative Flux")
gd2 = graph(title="distance plot",width=800,height=600,x=0,y=1200,xtitle="Time (Days)",ytitle="Distance (AU)")
gd3 = graph(title="velocity plot",width=800,height=600,x=0,y=1800,xtitle="Time (Days)",ytitle="Velocity (km/s)")

ft = gcurve(graph=gd,color=color.red)
rt = gcurve(graph=gd2,color=color.red)
vt = gcurve(graph=gd3,color=color.red)

scene.append_to_title("""
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, use scroll wheel.
""")
    

def g_f():
    r = sun.pos - planet.pos
    g_f = r*(G/(mag(r)**3))
    return g_f

def flux():
    rel_d = planet.pos - sun.pos
    rel_d_flatten = ((rel_d.x**2)+(rel_d.y**2))**0.5
    if rel_d_flatten > R_planet+R_sun or rel_d.z<0:
        return 1
    elif rel_d_flatten <= R_sun-R_planet:
        return 1 - (R_planet/R_sun)**2
    else:
        print(t/1440)
        A1 = (R_planet**2)*acos(((rel_d_flatten**2)+(R_planet**2)-(R_sun**2))/(2*rel_d_flatten*R_planet))
        A2 = (R_sun**2)*acos(((rel_d_flatten**2)+(R_sun**2)-(R_planet**2))/(2*rel_d_flatten*R_sun))
        A3 = 0.5*(((-rel_d_flatten+R_planet+R_sun)*(rel_d_flatten+R_planet-R_sun)*(rel_d_flatten-R_planet+R_sun)*(rel_d_flatten+R_planet+R_sun))**0.5)
        A = A1+A2-A3
        return (pi*(R_sun**2) - A)/(pi*(R_sun**2))


def setup():
    global sun, planet
    sun.pos = P0_sun
    planet.pos = P0_planet
    sun.v = V0_sun
    planet.v = V0_planet
    planet.clear_trail()
    ft.delete()
    rt.delete()
    vt.delete()



def update():
    global planet,sun,t,dt
    ft.plot(t/1440,flux())
    rt.plot(t/86400,mag(planet.pos-sun.pos)/AU)
    vt.plot(t/86400,mag(planet.v)/1000)


    #sun.a = -g_f()*M_planet
    planet.a = g_f()*M_sun
    #sun.v += sun.a*dt
    planet.v += planet.a*dt
    #sun.pos += sun.v*dt
    planet.pos += planet.v*dt
    t += dt

def run(b1):
    global running
    running = not running
    if running:
        b1.text = "Pause"
    else:
        b1.text = "Run"

b1 = button(text="Run", pos=scene.title_anchor, bind=run)

def reset(b2):
    global re
    re = not re
b2 = button(text="Reset", pos=scene.title_anchor, bind=reset)

def stop(b3):
    global end
    end = not end
b3 = button(text="Stop", pos=scene.title_anchor, bind=stop)

def reset_camera(b4):
    scene.camera.pos = scene_camera_original_pos
b4 = button(text="Reset Camera", pos=scene.title_anchor, bind=reset_camera)

setup()
while not end:
    rate(100)
    if running:
        update()
    if re:
        setup()
        re = not re
