from mpl_toolkits.basemap import Basemap

import numpy as n
import matplotlib.pyplot as plt


def read_coords(plot=False):
    f=file("e3d_core_outliers.txt")
    c=[]
    for li,l in enumerate(f.readlines()):
        row=l.split("\t")
        if li > 1 and len(row)>1:
            print(row)
            c.append(n.array([float(row[0]),float(row[1]),float(row[2])]))
    c=n.array(c)
    if plot:
        plt.plot(c[:,1],c[:,0],".",label="Outlier",markersize=24)
        plt.plot(c[0,1],c[0,0],".",label="Core",markersize=24)
        plt.legend()
        plt.xlabel("East-West position (m)")
        plt.ylabel("North-South position (m)")
        plt.title("EISCAT 3D core and outlier positions")
        plt.tight_layout()
        plt.show()
    
    return(c)


#read_coords(plot=True)
ski_lat=69.3908
ski_lon=20.2673
kar_lat=68.4490
kar_lon=22.4838
kai_lat=68.267
kai_lon=19.448
lat0=n.median(ski_lat)
lon0=n.median(ski_lon)

m=Basemap(projection="stere",
          lat_0=lat0,
          lon_0=lon0,
          llcrnrlat=66,
          urcrnrlat=72,
          llcrnrlon=11,
          urcrnrlon=32,
          resolution="h")
m.drawcoastlines()

pars=n.arange(67,72,2)
m.drawparallels(pars,labels=pars)

mers=n.arange(15,30,5)
m.drawmeridians(mers,labels=[1,0,0,1])

x,y=m(ski_lon,ski_lat)
plt.plot(x,y,".",label="Skibotn",markersize=24)
x,y=m(kar_lon,kar_lat)
plt.plot(x,y,".",label="Karesuvanto",markersize=24)
x,y=m(kai_lon,kai_lat)
plt.plot(x,y,".",label="Kaiseniemi",markersize=24)
plt.legend()
plt.title("EISCAT 3D Sites")
plt.tight_layout()

plt.show()
