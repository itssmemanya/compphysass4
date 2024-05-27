import numpy as np
import emcee
import corner
import matplotlib.pyplot as plt

def model(theta, x):
    a, b, c = theta
    return a * x**2 + b * x + c

def log_likelihood(theta, x, y, yerr):
    model_y = model(theta, x)
    return -0.5 * np.sum((y - model_y) ** 2 / yerr ** 2 + np.log(yerr ** 2))

def log_prior(theta):
    a, b, c = theta
    if -10 < a < 10 and -10 < b < 10 and -10 < c < 10:
        return 0.0
    return -np.inf

def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, yerr)

data = np.loadtxt('data.txt')
x = data[:, 1]
y = data[:, 2]
yerr = data[:, 3]

nwalkers = 50  # Number of Markov chains
ndim = 3       # Number of parameters (a, b, c)
nsteps = 4000  # Number of steps per chain


start = 1e-4 * np.random.randn(nwalkers, ndim)
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(x, y, yerr))
sampler.run_mcmc(start, nsteps, progress=True)
samples = sampler.get_chain()
flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
best_fit = np.median(flat_samples, axis=0)


print("Best-fit parameters:")
print(f"a = {best_fit[0]:.3f} ± {np.std(flat_samples[:, 0]):.3f}")
print(f"b = {best_fit[1]:.3f} ± {np.std(flat_samples[:, 1]):.3f}")
print(f"c = {best_fit[2]:.3f} ± {np.std(flat_samples[:, 2]):.3f}")


fig, axes = plt.subplots(3, sharex=True)
labels = ["a", "b", "c"]
colors = ["r", "g", "b"]  # Red for a, Green for b, Blue for c
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], color=colors[i], alpha=0.3)
    ax.set_xlim(0, nsteps)
    ax.set_ylabel(labels[i])
axes[-1].set_xlabel("Step number")
plt.show()

fig = corner.corner(flat_samples, labels=labels, truths=[best_fit[0], best_fit[1], best_fit[2]],
                    scatter_kwargs={"alpha": 0.5, "marker": "o"},
                    hist_kwargs={"linewidth": 1, "edgecolor": "black"},
                    label_kwargs={"fontsize": 12})
plt.show()

x_fit = np.linspace(min(x), max(x), 1000)
plt.errorbar(x, y, yerr=yerr, fmt=".k", capsize=0)

for theta in flat_samples[np.random.randint(len(flat_samples), size=200)]:
    plt.plot(x_fit, model(theta, x_fit), color="gray", alpha=0.1)

plt.xlabel("x_fit")
plt.ylabel("y_fit")
plt.title("Best fit along with  200 models randomly chosen from the posterior")
plt.plot(x_fit, model(best_fit, x_fit), label="Best fit", color='red')
plt.legend()
plt.show()
