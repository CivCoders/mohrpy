import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Cursor 

from math import sqrt, cos, sin, pi

print "\t==================================================="
print "\tMohrpy - Open source Mohr's Circle plotting program."
print "\t==================================================="
print ""
print ("\tEnter value of different stress for system of stress.")
print ("\t(-ve value for compressive stress.)")
print ("\tPress Ctrl+C for exit.\n\n")

sigma_x = eval(raw_input('>> Enter sigma_x: '))
sigma_y = eval(raw_input('>> Enter sigma_y: '))
theta = eval(raw_input('>> Enter angle of inclination (in degrees): '))

print ("  (Please enter 0 if tau_xy doesn't exists.)")

tau_xy = eval(raw_input('>> Enter tau_xy: '))

def deg2rad(theta):
	return pi/180*theta

def fsigma_n(sigma_x, sigma_y, theta, tau_xy):
	return (0.5*(sigma_x + sigma_y) + 
	0.5*(sigma_x - sigma_y)*cos(2*deg2rad(theta)) + 
	tau_xy*sin(2*deg2rad(theta)))

def ftau_n(sigma_x, sigma_y, theta, tau_xy):
	return (0.5*(sigma_x - sigma_y)*sin(2*deg2rad(theta))
		+ tau_xy*cos(2*deg2rad(theta)))

def fsigma_avg(sigma_x, sigma_y):
	return 0.5*(sigma_x + sigma_y)

def fradii(sigma_x, sigma_y, tau_xy):
	return sqrt((0.5*(sigma_x - sigma_y))**2 + tau_xy**2)

sigma_avg = fsigma_avg(sigma_x, sigma_y)
radii = fradii(sigma_x, sigma_y, theta)
print sigma_avg, radii

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

c1 = plt.Circle((sigma_avg, 0), radii, color='b', fill=False)
plt.gcf().gca().add_artist(c1)

plt.axis([ min(sigma_x, sigma_y) - 30, max(sigma_x, sigma_y) + 30, -radii -30, radii + 30])
plt.grid(True)

plt.title("Mohr's circle")
plt.xlabel('sigma_n -->')
plt.ylabel('tau_n  -->')

cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

axcolor = 'lightgoldenrodyellow'
ax_sigx = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
ax_sigy  = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
ax_tauxy = plt.axes([0.25, 0.05, 0.65, 0.03], axisbg=axcolor)

s_sigx = Slider(ax_sigx, 'sigma_x', sigma_x - 50, sigma_x + 50, valinit=sigma_x)
s_sigy = Slider(ax_sigy, 'sigma_y', sigma_y - 50, sigma_y + 50, valinit=sigma_y)
s_tauxy = Slider(ax_tauxy, 'tau_xy', 0, 360, valinit=tau_xy)

def update(val):
	sigma_x = s_sigx.val
	sigma_y = s_sigy.val
	tau_xy = s_tauxy.val
	sigma_avg = fsigma_avg(sigma_x, sigma_y)
	radii = fradii(sigma_x, sigma_y, tau_xy)
	c1.center=sigma_avg,0
	c1.radius=radii
	plt.axis([ min(sigma_x, sigma_y) - radii, max(sigma_x, sigma_y) + radii, -2*radii, 2*radii])
	fig.canvas.draw_idle()

s_sigx.on_changed(update)
s_sigy.on_changed(update)
s_tauxy.on_changed(update)

plt.show()