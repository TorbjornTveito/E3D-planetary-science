import horizons_planetary as hp
import numpy as n
import matplotlib.pyplot as plt

def plot_lines(lon,lat,gidx):
    ranges=[]
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
    

def moon_observability():
#    start = 2030
    plt.figure(figsize=(10,10))
    
    plt.subplot(331)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2022-01-01",
                      stop="2023-01-01")
    
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    #plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")
    plt.title("2022")
    
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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
    eph=hp.get_ephemeris(obj_id="301",
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


def moon_observability_2030():
    step = "30m"
#    start = 2030
    plt.figure(figsize=(10,10))
    
    plt.subplot(331)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2031-01-01",
                      stop="2032-01-01",
                      step=step
                      )
    
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    #plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")
    plt.title("2031")
    
    eph=hp.get_ephemeris(obj_id="301",
                      start="2032-01-01",
                      stop="2033-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]

    plt.subplot(332)
    plt.title("2032")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)    
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
#    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")
    

    plt.subplot(333)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2033-01-01",
                      stop="2034-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.title("2033")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)    
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
#    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")
    

    plt.subplot(334)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2034-01-01",
                      stop="2035-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.title("2034")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    #   plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(335)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2035-01-01",
                      stop="2036-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2035")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
 #   plt.xlabel("Sub-radar lunar longitude (deg)")
  #  plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(336)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2036-01-01",
                      stop="2037-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2036")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
   # plt.xlabel("Sub-radar lunar longitude (deg)")
   # plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(337)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2037-01-01",
                      stop="2038-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2037")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(338)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2038-01-01",
                      stop="2039-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2038")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
 #   plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(339)
    eph=hp.get_ephemeris(obj_id="301",
                      start="2039-01-01",
                      stop="2040-01-01",
                      step=step
                      )
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2039")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")

    
    plt.tight_layout()
    plt.show()

moon_observability()
moon_observability_2030()
