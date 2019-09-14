#!/usr/bin/python3

# Free Fall with Air Resistance by Jamie Chang

import matplotlib.pyplot as plt



#Variables
init_velocity = 100 #(m/s)
v = init_velocity
m = 1 #(kg)
g = 9.8 #(m/s^2)
b = 1 #(kg/s)
t = 0
duration = 50 #(s)
x_axis_range=(-3,duration)
y_axis_range=(-40,100)




#Main
################################
v_list = [v]
t_list = [0]

fig,ax = plt.subplots()

def setup():
    global t,v,v_list,t_list
    t = 0
    v = init_velocity
    v_list = [v]
    t_list = [0]

def draw(dt):
    setup()
    global t,v
    for i in range(int(duration/dt)):
        t += dt
        f = -b*v
        a = g + (f/m) #downward
        v += (a*dt)
        v_list.append(v)
        t_list.append(t)
    return v_list,t_list

ax.set_xlim((x_axis_range))
ax.set_ylim(y_axis_range)

draw(dt=0.01)
l1, = ax.plot(t_list,v_list,c="green",lw=0.8,label="dt = 0.01")

draw(dt=0.1)
l2, = ax.plot(t_list,v_list,c="#FFD800",lw=0.8,label="dt = 0.1")

draw(dt=0.5)
l3, = ax.plot(t_list,v_list,c="orange",lw=0.8,label="dt = 0.5")

draw(dt=1.5)
l4, = ax.plot(t_list,v_list,c="red",lw=0.8,label="dt = 1.5")

ax.set_facecolor("#CCFFFE")
ax.legend(handles=[l1,l2,l3,l4],loc="best")
ax.set_xlabel(r'$time\ (s)$')
ax.set_ylabel(r'$velocity\ (m/s , downward)$')
ax.set_title(r'$Free\ Fall\ with\ Air\ Resistance\ by\ Jamie\ Chang$')


plt.show()