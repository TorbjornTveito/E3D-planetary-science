#!/usr/bin/env python

import numpy as n
import scipy.constants as c
from astroquery.jplhorizons import Horizons
#import neo_snr
import matplotlib.pyplot as plt

def get_ephemeris(obj_id="2020 DA4",
                        obs_lat=69.3908,
                        obs_lon=20.2673,
                        obs_el=0.0,
                        start="2029-01-01",
                        stop="2030-01-01",
                        step="2h",
                        min_el=30.0,
                        id_type="majorbody",
                        debug=True):
    
    e3d = {'lon': obs_lon, 'lat': obs_lat, 'elevation': obs_el}
    obj = Horizons(id=obj_id,
                   location=e3d,
                   epochs={"start":start,
                           "stop":stop,
                           "step":step},
                   id_type=id_type)
#    print(obj)
    t0=obj.ephemerides(quantities="4,20,14",get_raw_response=True)
    
    t=obj.ephemerides(get_raw_response=True)
#    print(t)
    
    lines=t.split("\n")
    soe=False
    eoe=False
    dates=[]
    jdates=[]
    azs=[]
    els=[]
    sublon=[]
    sublat=[]
    r=[]
    rdot=[]
    for l in lines:
        if l.strip() == "$$EOE":
            eoe=True
        if soe and eoe == False:
            items=l.split(",")
            dates.append(items[0])
            jdates.append(float(items[1]))
            
            
            azs.append(float(items[10]))
            els.append(float(items[11]))
            sublon.append(float(items[27]))
            sublat.append(float(items[28]))
            r.append(float(items[39])*c.au)
            rdot.append(float(items[40]))
            
#            print(l)
        if l.strip() == "$$SOE":
            soe=True
    r=n.array(r)
    rdot=n.array(rdot)
    azs=n.array(azs)
    els=n.array(els)
    sublon=n.array(sublon)
    sublat=n.array(sublat)
    jdates=n.array(jdates)
    # convert to +/- lon
    sublon[sublon>180.0]=(360-sublon[sublon>180.0])*-1.0
    return({"r":r,"rdot":rdot,"az":azs,"el":els,"sublon":sublon,"sublat":sublat,"jdates":jdates,"dates":dates})

    


if __name__ == "__main__":
    pass
#    eph=check_detectability(obj_id="301",debug=True)
#    moon_observability()

    
