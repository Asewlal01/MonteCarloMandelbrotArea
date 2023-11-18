import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from QuasiMonteCarlo import quasiMC

# Get the data
i = 200  # iteration number
run_num = 5  # number of runs at each "s"
s_list = np.arange(5, 101, 2)
s_list = s_list**2  # list of "s"
data_QMC = np.zeros((len(s_list), run_num))
for j, s in enumerate(s_list):  # row: different s values
    for k in range(run_num):  # column: different runs
        data_QMC[j, k] = quasiMC(-2, 2, i, s)  # areas per run
deltaA_QMC = np.abs(data_QMC - data_QMC[-1, :])  # area difference

# Get the convergence iteration number
significance_level = 0.05
conv_i_QMC = 0
for s, deltaA in zip(s_list, deltaA_QMC):
    _, p_value = stats.ttest_ind(deltaA, deltaA_QMC[-1], equal_var=False)
    if p_value > significance_level:
        conv_i_QMC = s
        break
print("QMC:", conv_i_QMC)

# Prepare for plotting
std_QMC = np.std(data_QMC, axis=1)
mean_QMC = np.mean(deltaA_QMC, axis=1)

# Plot
fig, axes = plt.subplots(2, 1, figsize=(8, 8), dpi=300)
axes[0].set_title(f"Iterations={i}")
axes[0].set_xlabel("Samples")
axes[0].set_ylabel("$|A_{i,s}-A_{i,k}|$")
axes[0].plot(s_list, mean_QMC, label='Quasi Monte Carlo', c='b')
axes[0].grid()
axes[0].legend()
axes[1].set_xlabel("Samples")
axes[1].set_ylabel("Standard Deviation")
axes[1].plot(s_list, mean_QMC, label='Quasi Monte Carlo', c='b')
axes[1].grid()
axes[1].legend()
plt.show()
