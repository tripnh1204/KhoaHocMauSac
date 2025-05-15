import colour
from colour.plotting import *
from colour.colorimetry import sd_CIE_illuminant_D65

import matplotlib.pyplot as plt

sd = sd_CIE_illuminant_D65().copy().trim(400, 700)

plt.figure(figsize=(10, 3))
colour.plotting.plot_single_sd(sd, out_of_gamut_clipping=True, bounding_box=(400, 700, 0, 1.1))
plt.title("Phổ khả kiến CIE Band (400–700 nm)")
plt.show()
