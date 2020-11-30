import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import numpy as np
import pandas as pd
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.patches as mpatches
import cartopy.feature as cfeature


# -------------- Initialisation de la figure ---------------- #
fig = plt.figure(figsize=(10, 8))

# Frame global
left = -0.05
bottom = -0.05
width = 1.1
height = 1.05
rect = [left,bottom,width,height]
ax3 = plt.axes(rect)

# Frame map
left = 0
bottom = 0
width = 0.95
height = 0.95
rect = [left,bottom,width,height]
#ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(central_longitude=-5, central_latitude=-5))
ax = plt.axes(rect, projection=ccrs.SouthPolarStereo())
ax.stock_img()
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='gray', alpha=0.5, linestyle='--')
gl.yformatter = LATITUDE_FORMATTER


# -------------- Import des données ---------------- #
classements_hist_clean = pd.read_pickle("dataframes/classements_hist_clean.pkl")


# -------------- Légende ---------------- #
left = 0
bottom = 0.4
width = 0.16
height = 0.5
rect = [left,bottom,width,height]
rect = [left,bottom,width,height]
#ax5 = plt.axes(rect)

colors = sorted(cartopy.feature.COLORS.keys())
handles = []
names = []
for c in colors:
    patch = mpatches.Patch(color=cfeature.COLORS[c], label=c)
    handles.append(patch)
    names.append(c)


# -------------- Ajout des données de la course ---------------- #
skippers = classements_hist_clean['Skipper'].values
nb_skip = classements_hist_clean['Skipper'].nunique()

sub_skippers_liste = list(skippers)[0:nb_skip-1]
sub_skippers_select = sub_skippers_liste[:3] + sub_skippers_liste[-3:]

for skipper in sub_skippers_select:

    classement_skip = classements_hist_clean[classements_hist_clean['Skipper']==skipper]
    lon = classement_skip['Longitude']
    lat = classement_skip['Latitude']
    bateau = classement_skip['Bateau'].unique()[0]
    position = classement_skip['Position'].unique()[0]

    plot_skip = ax.plot(lon, lat,
            linestyle='-',
            transform=ccrs.Geodetic(),
            label = f'{skipper} #{position}'
            )
    handles.append(plot_skip)
    names.append(skipper)


#ax.set_global()
ax.coastlines()
ax.gridlines()
ax.legend(loc='upper left', prop={'size': 6})
ax.set_extent([-50, 10, -50, 50])
plt.show()