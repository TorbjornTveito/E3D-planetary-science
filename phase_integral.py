from __future__ import division

import numpy as np
import scipy.constants as c
import matplotlib.pyplot as plt
import scipy.interpolate as intp
import scipy.integrate as integ

def lineintegral(function, xmin, xmax, ymin, ymax, points): #integrates over a line. shittily 
    xline = np.linspace(xmin, xmax, points)
    yline = np.linspace(ymin, ymax, points)
    result = 0
    for i in range(points):
        result += function(xline[i],yline[i])*np.sqrt(((xmax - xmin)/points)**2 + ((ymax - ymin)/points)**2)*1E3 #assumes kilometers
    result = float(result)
    return(result)

def horizontal_scale(background, wavenumber, frequency, amplitude, scale, time, tid_angle, tecu_scale): #creates a horizonally np.sinusoidal ionosphere ***BEMERKNING*** the ionosphere is the time-derivative of an ionosphere with TIDs
    yax = np.linspace(100, 1000, 91)
    xax = np.linspace(0, 2000, 1000)

    xx, yy = np.meshgrid(xax, yax)

    kx = wavenumber*np.cos(tid_angle/180*np.pi)
    ky = wavenumber*np.sin(tid_angle/180*np.pi)

    el2d = background(yy)*(tecu_scale*amplitude*np.cos(ky*2*np.pi*(yy-100)+kx*2*np.pi*xx - frequency*time*2*np.pi) )

    el2d = intp.interp2d(xax, yax, el2d)
    return(el2d)

alpha = 0.10 #TID amplitude
radar_freq = 230E6 #radar frequency
wave_freq = 1.0/600.0 #wave temporal frequency
wavenum = 1.0/200.0 #wave spatial frequency
look_angle = 45 #look angle
dif = 0.25 #target angular radius
tid_angle = 45
###initial values

f = open("ref_iono.txt", "r")

electrons = []
height = []


a = c.elementary_charge**2/(c.epsilon_0 * c.electron_mass * radar_freq * c.c*2*np.pi)

xinit = 250

line = f.readline().split()
while line[0] != "end": #reading electron density profile
    electrons.append((float(line[1])))
    height.append(float(line[0]))
    line = f.readline().split()
electrons = intp.interp1d(height, electrons)
elect2d = horizontal_scale(electrons, wavenum, wave_freq, alpha, 1000, 0, tid_angle, tecu_scale = 2) #creating test ionosphere

yaxis, xaxis = np.mgrid[100:1010:10, 0:2000:2] #pcolormesh nonsense
yax = np.linspace(100, 1000, 91) #axes of some sort
xax = np.linspace(0, 2000, 1000)

plot = 1 # 1 to see time-derivative of ionosphere

line30deg = np.array([np.linspace(xinit,xinit+900/np.sin(30/180*np.pi)*np.cos(30/180*np.pi), 2), np.linspace(100, 1000, 2)])
line45deg = np.array([np.linspace(xinit,xinit+900/np.sin(45/180*np.pi)*np.cos(45/180*np.pi), 2), np.linspace(100, 1000, 2)])
arrow_pos = [1115, 350]
arrow_dir = [1, 1]
arrow_length = 100


if plot == 1:
    plt.pcolormesh(xaxis, yaxis, elect2d(xax, yax), cmap = 'inferno')
    plt.title("Electron enhancements due to TID, perpend. front", fontsize = 12)
    plt.xlabel("Horizontal distance (km)", fontsize = 12)
    plt.ylabel("Height (km)", fontsize = 12)
    plt.plot(line30deg[0], line30deg[1], label = '30 degrees', color = "blue")
    plt.plot(line45deg[0], line45deg[1], label = '45 degrees', color = "white")
    plt.arrow(arrow_pos[0], arrow_pos[1], arrow_dir[0]*arrow_length,arrow_dir[1]*arrow_length, width = 10, color = 'cyan')
    plt.tight_layout()
    plt.legend()
    plt.colorbar()
    plt.savefig("ionosphere_mod90")
    plt.show()

x_dist = 900/np.sin(look_angle/180*np.pi)*np.cos(look_angle/180*np.pi)

timeax = np.linspace(0, 1200, 40) #prepping time

integrated_electrons = []
integrated_electrons2 = []
integrated_electrons3 = []
test = []
for times in timeax: #creating time dependence
    integrated_electrons.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, alpha, 1000, times, tid_angle, tecu_scale=2), xinit, xinit+900/np.sin(look_angle/180*np.pi)*np.cos(look_angle/180*np.pi), 100, 1000, 100))
    integrated_electrons2.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, alpha, 1000, times, tid_angle, tecu_scale=2), xinit, xinit+900/np.sin(look_angle/180*np.pi)*np.cos((look_angle+dif)/180*np.pi), 100, 1000, 100))
    integrated_electrons3.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, alpha, 1000, times, tid_angle, tecu_scale=2), xinit, xinit+900/np.sin(look_angle/180*np.pi)*np.cos((look_angle-dif)/180*np.pi), 100, 1000, 100))

integrated_electrons = np.array(integrated_electrons) #making arrays
integrated_electrons2 = np.array(integrated_electrons2)
integrated_electrons3 = np.array(integrated_electrons3)

plt.plot(integrated_electrons*10**(-16))
plt.show()

phases = np.array(integrated_electrons*a)
phases2 = integrated_electrons2*a
phases3 = integrated_electrons3*a

if plot == 1:
    plt.plot(timeax, phases, label = "sub-radar point")
    plt.plot(timeax, phases2, label = "'zenith' limb" )
    plt.plot(timeax, phases3, label = "'horizon' limb")
    plt.title("change in frequency due to ionospheric time dependence")
    plt.show()

    plt.plot(timeax, (phases2 - phases))
    plt.title("doppler broadening RELATIVE TO subradar point")
    plt.show()


timeax = np.linspace(0, 1200, 40) #prepping time
angles = np.array([30, 45, 60, 75])

alpha_1_tecu_10 = []
alpha_5_tecu_10 = []
alpha_10_tecu_10 = []
alpha_1_tecu_40 = []
alpha_5_tecu_40 = []
alpha_10_tecu_40 = []

if 0:

    for times in timeax:
        alpha_1_tecu_10.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.01, 1000, times, tid_angle, tecu_scale=2), xinit, xinit + x_dist, 100, 1000, 100))
        alpha_5_tecu_10.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.05, 1000, times, tid_angle, tecu_scale=2), xinit, xinit + x_dist, 100, 1000, 100))
        alpha_10_tecu_10.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.1, 1000, times, tid_angle, tecu_scale=2), xinit, xinit + x_dist, 100, 1000, 100))
        alpha_1_tecu_40.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.01, 1000, times, tid_angle, tecu_scale=8), xinit, xinit + x_dist, 100, 1000, 100))
        alpha_5_tecu_40.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.05, 1000, times, tid_angle, tecu_scale=8), xinit, xinit + x_dist, 100, 1000, 100))
        alpha_10_tecu_40.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.1, 1000, times, tid_angle, tecu_scale=8), xinit, xinit + x_dist, 100, 1000, 100))

    alpha_1_tecu_10 = np.array(alpha_1_tecu_10)*a
    alpha_5_tecu_10 = np.array(alpha_5_tecu_10)*a
    alpha_10_tecu_10 = np.array(alpha_10_tecu_10)*a
    alpha_1_tecu_40 = np.array(alpha_1_tecu_40)*a
    alpha_5_tecu_40 = np.array(alpha_5_tecu_40)*a
    alpha_10_tecu_40 = np.array(alpha_10_tecu_40)*a

    broadening_1_10 = max(alpha_1_tecu_10)- min(alpha_1_tecu_10)
    broadening_5_10 = max(alpha_5_tecu_10)- min(alpha_1_tecu_10)
    broadening_10_10 = max(alpha_10_tecu_10)- min(alpha_10_tecu_10)
    broadening_1_40 = max(alpha_1_tecu_40)- min(alpha_1_tecu_40)
    broadening_5_40 = max(alpha_5_tecu_40)- min(alpha_5_tecu_40)
    broadening_10_40 = max(alpha_10_tecu_40)- min(alpha_10_tecu_40)


    print(broadening_1_10,broadening_1_10/3.2*100, "1, 10")
    print(broadening_5_10,broadening_5_10/3.2*100, "5, 10")
    print(broadening_10_10,broadening_10_10/3.2*100, "10, 10")
    print(broadening_1_40,broadening_1_40/3.2*100, "1, 40")
    print(broadening_5_40,broadening_5_40/3.2*100, "5, 40")
    print(broadening_10_40,broadening_10_40/3.2*100, "10, 40")

if 0:
    angles = np.linspace(0, 90, 7)-45
    for angle in angles:
        alpha_10_tecu_40 = 0
        alpha_10_tecu_40 = []
        for times in timeax:
            alpha_10_tecu_40.append(lineintegral(horizontal_scale(electrons, wavenum, wave_freq, 0.1, 1000, times, angle, tecu_scale=8), xinit, xinit + x_dist, 100, 1000, 100))
        
        alpha_10_tecu_40 = np.array(alpha_10_tecu_40)*a
        broadening_10_40 = max(alpha_10_tecu_40)- min(alpha_10_tecu_40)
        
        print(broadening_10_40,broadening_10_40/3.2*100, angle+45)