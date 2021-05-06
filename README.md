# E3D-planetary-science
Code repository for E3D planetary science article

ref_iono.txt contains electron density profile data based on the international reference ionosphere (see http://irimodel.org/). This electron density profile is then scaled to a desired vertical TEC.
The program phase_integral.py then calculates the frequency modulating effects of variable TEC.

The program plot_stations.py plots the outliers and main station sites for the EISCAT 3D facility. 

The program planet_observability.py uses the HORIZONS ephemeris to find best-case signal-to-noise ratios for the three terrestrial planets and the Moon.

The program moon_observability.py uses the HORIZONS ephemeris to find possible observation opportunities for the Moon in the years 2022-2040, and plots the sub-radar point during this period. 
