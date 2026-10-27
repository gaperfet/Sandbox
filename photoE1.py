import random
import time

import numpy as np
from matplotlib import pyplot as plt

num_photons = 10000
E_0 = 6000. # eV
W_i = 30. # eV
G = 100.

pha = []
t0 = time.time()

# Outer loop over the impinging X-rays.
for i in range(num_photons):
    # Initialize the total number of the electron-ion pairs that are created
    # by ionization for this particular event.
    total_ionization = 0
    # Extract the number of primary electrons created by the photoelectron.
    # Too bad the random module in the standard lib does not provide the
    # Poisson distribution, and we do have to resort to numpy...
    num_primaries = np.random.poisson(E_0 / W_i)
    # Inner loop over the primary electrons...
    for j in range(num_primaries):
        # For each primary electron, extract the number of electron-ion pairs
        # generated in the avalanche.
        total_ionization += random.expovariate(1. / G)
    pha.append(total_ionization)

dt = time.time() - t0
plt.hist(pha, bins=np.linspace(12500., 27500., 50))
plt.xlabel("Pulse height [electrons]")
plt.ylabel("Counts per bin")
plt.title(f"Pulse height spectrum ({num_photons} photons)")
plt.tight_layout()
plt.savefig("pha_spectrum.png", dpi=300)
plt.show()
print(f"Simulation completed in {dt:.3f} s")