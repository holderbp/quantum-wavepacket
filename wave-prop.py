import numpy as np
import matplotlib.pyplot as plt

#
# physical parameters of sum of two momentum eigenstates
#
#   <x|p> = 1/sqrt(2 pi hbar) * exp[ i p/hbar x ]
#
#   <x|psi> = A * <x|p> + B * <x|(p+dp)>      dp << p
#
p = 1
dp_over_p = 0.1
dp = p * dp_over_p
hbar = 1
m = 1
A = 1
B = 1

#
# plotting pars
#
npoints = 1000
xlength_in_lambda_env = 2.5
tmax = 100
dt = 0.1
plot_interval_sec = 0.05

def get_xvals():
    return np.linspace(0, xmax, num=npoints)

def get_psi(x, t):
    return (
        A * np.exp(- 1j/hbar * (p**2 / 2 / m) * t) * np.exp( 1j/hbar * (p/hbar) * x)
        + B * np.exp(- 1j/hbar * ((p+dp)**2 / 2 / m) * t) * np.exp( 1j/hbar * ((p+dp)/hbar) * x)
        )

###############
# Main Code
###############

# get wavelengths, create position array
lambda_carrier = 2*np.pi / (p / hbar)
lambda_envelope =  2*np.pi / (dp / hbar)
xmax = xlength_in_lambda_env * lambda_envelope
x = get_xvals()
# set up figure
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8,4))
# loop over times and replot
for t in range(int(tmax/dt)):
    psi = get_psi(x,t)
    ax[0].plot(x, np.real(psi))
    ax[1].plot(x, np.imag(psi))
    # dress up plot
    ax[0].set_title(r"Sum of two momentum eigenstates $|p\rangle$ and $|p + dp \rangle$, with "
                    + f"dp = {dp_over_p:.2f} p")
    ax[0].set_ylabel(r'${\rm Re}\left[\psi(x,t)\right]$')
    ax[1].set_ylabel(r'${\rm Im}\left[\psi(x,t)\right]$')
    ax[1].set_xlabel(r'$x$')
    # draw and pause
    fig.canvas.draw()
    plt.pause(plot_interval_sec)
    # clear before next plot
    ax[0].clear()
    ax[1].clear()      
