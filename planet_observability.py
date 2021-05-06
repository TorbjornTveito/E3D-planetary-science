import horizons_planetary as hp
import numpy as n
import matplotlib.pyplot as plt
import scipy.constants as c
import neo_snr as ns

def plot_lines(lon,lat,gidx):
    ranges=[]
    if len(gidx)<1:
        return
    i0=gidx[0]
    i1=gidx[0]
    for i in range(len(gidx)-1):
        if gidx[i+1]-gidx[i] == 1:
            i1=gidx[i+1]
        else:
            ranges.append((i0,i1))
            i0=gidx[i+1]
        
    for r in ranges:
        print("%d-%d"%(r[0],r[1]))
        plt.plot(lon[r[0]:r[1]],lat[r[0]:r[1]],color="green")


def snr(radar,
        oid="499",
        start="2035-Aug-14",
        R=3389.5e3,
        stop="2036-Feb-15"):

    gain0=radar.gain
    
    eph=hp.get_ephemeris(obj_id=oid,
                         start=start,
                         stop=stop,
                         step="1h")


    plt.subplot(121)
    plt.plot(eph["jdates"],eph["el"])
    plt.xlabel("Julian year")
    plt.ylabel("Elevation")
    
    plt.subplot(122)
    plt.plot(eph["jdates"],eph["r"])
    plt.xlabel("Julian year")
    plt.ylabel("Range (km)")
    
    plt.show()
    
    x=R*n.cos(n.pi*eph["sublat"]/180.0)*n.sin(n.pi*eph["sublon"]/180.0)
    y=R*n.cos(n.pi*eph["sublat"]/180.0)*n.cos(n.pi*eph["sublon"]/180.0)
    z=R*n.sin(n.pi*eph["sublat"]/180.0)
    t_s=eph["jdates"]*24*3600.0
    dt=n.diff(t_s)
    # apparent rotation velocity
    vel=n.sqrt((n.diff(x)/dt)**2.0+(n.diff(y)/dt)**2.0+(n.diff(z)/dt)**2.0)
    # limb-to-limb velocity extent
    dop_vel=2*vel

    # where is it sufficiently above the horizon
    gidx=n.where(eph["el"] > 30.0)[0]
    gidx=gidx[0:(len(gidx)-1)]
    
    plt.plot(vel,".")
    plt.plot(gidx,vel[gidx],".")
    plt.xlabel("Julian date")
    plt.ylabel("Apparent rotation velocity (m/s)")
    plt.show()

    
    mi=gidx[n.argmin(eph["r"][gidx])]
    vel0=vel[mi]
    el0=eph["el"][mi]
    radar.gain=gain0*n.sin(n.pi*el0/180.0)
    range0=eph["r"][mi]
    spin_period=2*n.pi*R/vel0


    
    o = ns.space_object(diameter_m=2.0*R,
                        range_m=range0,
                        spin_period_s=spin_period,
                        radar_albedo=0.1)
    

    snr_coh,snr_incoh=ns.detectability(radar, o, t_obs=3600.0, debug=True)
    print("%s r %1.1g snr_coh %1.2f snr_incoh %1.2f"%(eph["dates"][mi],range0,10.0*n.log10(snr_coh),10.0*n.log10(snr_incoh)))


def best_observing_date(oid="499",step="2d",start="2020-01-01",stop="2040-01-01"):
    eph=hp.get_ephemeris(obj_id=oid,
                         start=start,
                         stop=stop,
                         step=step)
    
    jd2y=(eph["jdates"]-eph["jdates"][0])/365.25 + 2020
    idx=n.argmin(eph["r"])
    print(eph["dates"][idx])
    
    gidx=n.where(eph["el"]>30.0)[0]
    idx0=n.argmin(eph["r"][gidx])
    idx0=gidx[idx0]
    print("closes range %1.2g @ %s above 30 %1.2g @ %s"%(eph["r"][idx],eph["dates"][idx],eph["r"][idx0],eph["dates"][idx0]))
    
    plt.plot(jd2y,eph["r"])
    gidx=n.where(eph["el"]>30.0)
    plt.plot(jd2y[gidx],eph["r"][gidx],".")
    plt.xlabel("Year")
    plt.ylabel("Range (km)")
    plt.show()


    


def planet_observability(oid="499"):


    eph=hp.get_ephemeris(obj_id=oid,
                         start="2020-01-01",
                         stop="2040-01-01",
                         step="1d")
    
    jd2y=(eph["jdates"]-eph["jdates"][0])/365.25 + 2020
    idx=n.argmin(eph["r"])
    print(eph["dates"][idx])
    plt.plot(jd2y,eph["r"])
    gidx=n.where(eph["el"]>30.0)
    plt.plot(jd2y[gidx],eph["r"][gidx],".")
    plt.xlabel("Year")
    plt.ylabel("Range (km)")
    plt.show()

    
    plt.figure(figsize=(10,10))
    
    plt.subplot(331)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2022-01-01",
                      stop="2023-01-01")
    
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    #plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")
    plt.title("2022")
    
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2023-01-01",
                      stop="2024-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.subplot(332)
    plt.title("2023")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)    
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
#    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")
    

    plt.subplot(333)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2024-01-01",
                      stop="2025-01-01")
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.title("2024")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)    
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
#    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")
    

    plt.subplot(334)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2025-01-01",
                      stop="2026-01-01")
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.title("2025")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    #   plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(335)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2026-01-01",
                      stop="2027-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2026")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
 #   plt.xlabel("Sub-radar lunar longitude (deg)")
  #  plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(336)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2027-01-01",
                      stop="2028-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2027")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
   # plt.xlabel("Sub-radar lunar longitude (deg)")
   # plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(337)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2028-01-01",
                      stop="2029-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2028")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(338)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2029-01-01",
                      stop="2030-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2029")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
 #   plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(339)
    eph=hp.get_ephemeris(obj_id=oid,
                      start="2030-01-01",
                      stop="2031-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2030")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")

    
    plt.tight_layout()
    plt.show()


e3d=ns.radar(gain=10**4.3,
             tx_pwr=5e6,
             duty_cycle=0.25,
             wavelength=1.3,
             noise_temp=200.0)

def moon():
    print("Moon")
    best_observing_date(oid="301",start="2022-01-01",stop="2023-01-01",step="1h")
    snr(e3d,oid="301",start="2022-01-01",stop="2023-01-01",R=1737e3)

def mars():
    print("Mars")
#    best_observing_date(oid="499",start="2022-01-01",stop="2030-01-01",step="4h")
    snr(e3d,oid="499",start="2022-11-01",stop="2023-02-01",R=3389.5e3)

def venus():
    print("Venus")
    best_observing_date(oid="299",start="2022-01-01",stop="2030-01-01",step="4h")
    snr(e3d,oid="299",start="2025-03-01",stop="2025-04-01",R=6051.8e3)

def mercury():
    print("Mercury")
    best_observing_date(oid="199",start="2022-01-01",stop="2030-01-01",step="4h")
    snr(e3d,oid="199",start="2028-06-01",stop="2028-07-01",R=2440e3)
    
    
moon()
mars()
venus()
mercury()
    
# mars = 499
# moon = 301
#planet_observability(oid="499")

#best_observing_date(oid="499")
#best_observing_date(oid="499",start="2035-Jun-01",stop="2036-Jun-01",step="2h")




