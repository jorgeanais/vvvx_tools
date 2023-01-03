import ligo.skymap.plot
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits
from matplotlib import pyplot as plt

hdu = fits.open("/home/jorge/Dropbox/develop/vvvx_plot_regions/density_map.fits")[1]
hdu.header["COORDSYS"] = 'GALACTIC'


ax = plt.axes(projection="galactic mollweide")
ax.grid()
ax.imshow_hpx(hdu, cmap="Greys")
plt.show()
