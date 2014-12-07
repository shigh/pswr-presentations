# Copied in from pywaveform/pswr-analysis.ipynb

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
matplotlib.rcParams.update({'font.size': 22})

# Maximum efficiency
Nt = 100.
K_vals = np.array([2.**p for p in range(4, 7)])
L_vals = np.array([2.**p for p in range(5)])
for k in K_vals:
    plt.plot(L_vals, k/L_vals*Nt/(k/L_vals*Nt+L_vals-1), 
             label="K=%i" % k, linewidth=2.0)

plt.legend(loc='lower left')
plt.xlabel("$L$")
plt.ylabel("Maximum Eff")

plt.savefig("./max_eff.png", transparent=True)

