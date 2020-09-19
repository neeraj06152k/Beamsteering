# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:32:14 2020

@author: Neeraj R
"""


import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import rel_sphe_coord as rsc


##############################################################################
# Corner points of the Contour and position of GSAT15

cape_lat, cape_lon = 8.083912, 77.545423
jam_lat, jam_lon = 22.491721, 70.029268
snar_lat, snar_lon = 34.037010, 74.846302
ghy_lat, ghy_lon = 26.183539, 91.756930

elv = 5.0e2
earth_radius = 6.378e6


gsat15_lon = 93.5
gsat15_elv = 3.5782e7 

##############################################################################
# Spherical Coordinates in degrees
# Format: S = (radius, Latitude_polar, Longitude_azimuth)

cape= (earth_radius+elv, 90.0-cape_lat, cape_lon)
jam= (earth_radius+elv, 90.0-jam_lat, jam_lon)
snar= (earth_radius+elv, 90.0-snar_lat , snar_lon)
ghy= (earth_radius+elv, 90.0-ghy_lat, ghy_lon)
gsat15= (earth_radius+gsat15_elv, 90.0, gsat15_lon)

##############################################################################
# Map and the Contour 
land_110m = cfeature.NaturalEarthFeature('physical', 'land', '110m',
                                        edgecolor='k',
                                        facecolor=cfeature.COLORS['land'])
extent = [65, 100, 40, -10]
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent)
ax.gridlines()
ax.stock_img()
ax.add_feature(land_110m)
#ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)


plt.plot([65.0, 100.0], [0.0, 0.0],
         color='black', linestyle='--',
         transform=ccrs.PlateCarree(),
         alpha=.9,
         )


plt.plot([65.0, 100.0], [23.4366, 23.4366],
         color='black', linestyle='--',
         transform=ccrs.PlateCarree(),
         alpha=.7,
         )



plt.plot([cape_lon, jam_lon], [cape_lat, jam_lat],
         color='blue', linestyle='--',
         transform=ccrs.PlateCarree(),
         alpha=.7,
         )

plt.plot([snar_lon, jam_lon], [snar_lat, jam_lat],
         color='blue', linestyle='--',
         transform=ccrs.PlateCarree(),
         alpha=.7,
         )

plt.plot([snar_lon, ghy_lon], [snar_lat, ghy_lat],
         color='blue', linestyle='--',
         transform=ccrs.PlateCarree(),
         alpha=.7,
         )

plt.plot([cape_lon, ghy_lon], [cape_lat, ghy_lat],
         color='blue', linestyle='--',
         transform=ccrs.PlateCarree(),
         alpha=.7,
         )

ax.coastlines(resolution='110m')


ax.plot(gsat15_lon, 0.0, 
        'gD', markersize=5, transform=ccrs.Geodetic())
ax.text(gsat15_lon - 7.0, -3.0, 
        'GSAT 15', fontsize=10, transform=ccrs.Geodetic())


ax.plot(cape_lon, cape_lat, 
        'go', markersize=2, transform=ccrs.Geodetic())
ax.text(cape_lon, cape_lat - 3.0, 
        'Kanyakumari', fontsize=8, transform=ccrs.Geodetic())

ax.plot(jam_lon, jam_lat, 
        'go', markersize=2, transform=ccrs.Geodetic())
ax.text(jam_lon - 1.0, jam_lat - 3.0, 
        'Jamnagar', fontsize=8, transform=ccrs.Geodetic())

ax.plot(snar_lon, snar_lat, 
        'go', markersize=2, transform=ccrs.Geodetic())
ax.text(snar_lon - 3.0, snar_lat + 1.0, 
        'Srinagar', fontsize=8, transform=ccrs.Geodetic())

ax.plot(ghy_lon, ghy_lat, 
        'go', markersize=2, transform=ccrs.Geodetic())
ax.text(ghy_lon - 3.0, ghy_lat + 1.0, 
        'Guwahati', fontsize=8, transform=ccrs.Geodetic())

##############################################################################
# Relative Coordinates of GSAT15 from the Four Corners
cape_gsat15 = rsc.rel_coord(cape, gsat15)
jam_gsat15 = rsc.rel_coord(jam, gsat15)
snar_gsat15 = rsc.rel_coord(snar, gsat15)
ghy_gsat15 = rsc.rel_coord(ghy, gsat15)

print(cape_gsat15, '\n',
      jam_gsat15, '\n',
      snar_gsat15, '\n',
      ghy_gsat15, '\n')
##############################################################################
# Coordinates of GSAT15 of the Local Spherical Coordinate System

cape_gsat15_local = [cape_gsat15[0],
                     cape_gsat15[1] - 90.0 + cape_lat,
                     cape_gsat15[2] - cape_lon]

jam_gsat15_local = [jam_gsat15[0],
                    jam_gsat15[1] - 90.0 + jam_lat,
                    jam_gsat15[2] - jam_lon]

snar_gsat15_local = [snar_gsat15[0] ,
                     snar_gsat15[1] - 90.0 + snar_lat,
                     snar_gsat15[2] - snar_lon]

ghy_gsat15_local = [ghy_gsat15[0],
                    ghy_gsat15[1] - 90.0 + ghy_lat,
                    ghy_gsat15[2] - ghy_lon]


##############################################################################
# Beam Steering angles from Four Corners towards GSAT15
bsteer_cape = [cape_gsat15_local[1], cape_gsat15_local[2]]
bsteer_jam = [jam_gsat15_local[1], jam_gsat15_local[2]]
bsteer_snar = [snar_gsat15_local[1], snar_gsat15_local[2]]
bsteer_ghy = [ghy_gsat15_local[1], ghy_gsat15_local[2]]

print('\n','Polar and Azimuth angles of the Beam pointing towards the GSAT15 for\n',
      'Antennas at respective places are:-\n',
      '(NOTE - The Format followed here is [polar, azimuth] in Degree)\n',sep='')
print('\tKanyakumari:', bsteer_cape, '\n',
      '\tJamnagar   :', bsteer_jam, '\n',
      '\tSrinagar   :', bsteer_snar, '\n',
      '\tGuwahati   :', bsteer_ghy, '\n', sep='')