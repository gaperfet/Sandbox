import time

import numpy as np
from matplotlib import pyplot as plt

rng = np.random.default_rng()

num_photons = 10000
E_0 = 6000. # eV
W_i = 30. # eV
G = 100.


t0 = time.time()

# Create an array with the number of primaries for each single X-ray.
num_primaries = rng.poisson(E_0 / W_i, size=num_photons)
# Populate an array with as many copies of the event id as the corresponding
# primary electrons
event_id = np.repeat(np.arange(num_photons), num_primaries)
# Extract the gain for each single primary electron.
event_gain = rng.exponential(scale=G, size=event_id.size)
# Sum all the ionization pairs, on an event-by-event basis, to get the "energy".
pha = np.bincount(event_id, weights=event_gain, minlength=num_photons)

dt = time.time() - t0
plt.hist(pha, bins=np.linspace(12500., 27500., 50))
plt.xlabel("Pulse height [electrons]")
print(f"Simulation completed in {dt:.3f} s")