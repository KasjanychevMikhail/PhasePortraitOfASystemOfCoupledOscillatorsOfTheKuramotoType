import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rhs(s, v):
    return [-1 + 0.2 * ((-np.sin(v[0] - v[0] + 1.6) + 0.2 * np.sin(2 * (v[0] - v[0]) - 1.58)) +
                       (-np.sin(v[0] - v[1] + 1.6) + 0.2 * np.sin(2 * (v[0] - v[1]) - 1.58)) +
                       (-np.sin(v[0] - v[2] + 1.6) + 0.2 * np.sin(2 * (v[0] - v[2]) - 1.58)) +
                       (-np.sin(v[0] - v[3] + 1.6) + 0.2 * np.sin(2 * (v[0] - v[3]) - 1.58)) +
                       (-np.sin(v[0] - v[4] + 1.6) + 0.2 * np.sin(2 * (v[0] - v[4]) - 1.58))),
            0 + 0.2 * ((-np.sin(v[1] - v[0] + 1.6) + 0.2 * np.sin(2 * (v[1] - v[0]) - 1.58)) +
                       (-np.sin(v[1] - v[1] + 1.6) + 0.2 * np.sin(2 * (v[1] - v[1]) - 1.58)) +
                       (-np.sin(v[1] - v[2] + 1.6) + 0.2 * np.sin(2 * (v[1] - v[2]) - 1.58)) +
                       (-np.sin(v[1] - v[3] + 1.6) + 0.2 * np.sin(2 * (v[1] - v[3]) - 1.58)) +
                       (-np.sin(v[1] - v[4] + 1.6) + 0.2 * np.sin(2 * (v[1] - v[4]) - 1.58))),
            1 + 0.2 * ((-np.sin(v[2] - v[0] + 1.6) + 0.2 * np.sin(2 * (v[2] - v[0]) - 1.58)) +
                       (-np.sin(v[2] - v[1] + 1.6) + 0.2 * np.sin(2 * (v[2] - v[1]) - 1.58)) +
                       (-np.sin(v[2] - v[2] + 1.6) + 0.2 * np.sin(2 * (v[2] - v[2]) - 1.58)) +
                       (-np.sin(v[2] - v[3] + 1.6) + 0.2 * np.sin(2 * (v[2] - v[3]) - 1.58)) +
                       (-np.sin(v[2] - v[4] + 1.6) + 0.2 * np.sin(2 * (v[2] - v[4]) - 1.58))),
            2 + 0.2 * ((-np.sin(v[3] - v[0] + 1.6) + 0.2 * np.sin(2 * (v[3] - v[0]) - 1.58)) +
                       (-np.sin(v[3] - v[1] + 1.6) + 0.2 * np.sin(2 * (v[3] - v[1]) - 1.58)) +
                       (-np.sin(v[3] - v[2] + 1.6) + 0.2 * np.sin(2 * (v[3] - v[2]) - 1.58)) +
                       (-np.sin(v[3] - v[3] + 1.6) + 0.2 * np.sin(2 * (v[3] - v[3]) - 1.58)) +
                       (-np.sin(v[3] - v[4] + 1.6) + 0.2 * np.sin(2 * (v[3] - v[4]) - 1.58))),
            3 + 0.2 * ((-np.sin(v[4] - v[0] + 1.6) + 0.2 * np.sin(2 * (v[4] - v[0]) - 1.58)) +
                       (-np.sin(v[4] - v[1] + 1.6) + 0.2 * np.sin(2 * (v[4] - v[1]) - 1.58)) +
                       (-np.sin(v[4] - v[2] + 1.6) + 0.2 * np.sin(2 * (v[4] - v[2]) - 1.58)) +
                       (-np.sin(v[4] - v[3] + 1.6) + 0.2 * np.sin(2 * (v[4] - v[3]) - 1.58)) +
                       (-np.sin(v[4] - v[4] + 1.6) + 0.2 * np.sin(2 * (v[4] - v[4]) - 1.58)))]

def drawPhasePortrait(args):
    res = solve_ivp(rhs, (args[0], args[1]), [4.8, 3, 2.2, 0, 1])
    axs[0, 0].plot(res.y[0].T, res.y[1].T, 'b')
    axs[0, 1].plot(res.y[0].T, res.y[2].T, 'b')
    axs[0, 2].plot(res.y[0].T, res.y[4].T, 'b')
    axs[1, 0].plot(res.y[1].T, res.y[2].T, 'b')
    axs[1, 1].plot(res.y[1].T, res.y[4].T, 'b')
    axs[1, 2].plot(res.y[2].T, res.y[4].T, 'b')

    axs[0, 0].set(xlabel='theta1')
    axs[0, 0].set(ylabel='theta2')
    axs[0, 0].grid()
    axs[0, 1].set(xlabel='theta1')
    axs[0, 1].set(ylabel='theta3')
    axs[0, 1].grid()
    axs[0, 2].set(xlabel='theta1')
    axs[0, 2].set(ylabel='theta5')
    axs[0, 2].grid()
    axs[1, 0].set(xlabel='theta2')
    axs[1, 0].set(ylabel='theta3')
    axs[1, 0].grid()
    axs[1, 1].set(xlabel='theta2')
    axs[1, 1].set(ylabel='theta5')
    axs[1, 1].grid()
    axs[1, 2].set(xlabel='theta3')
    axs[1, 2].set(ylabel='theta5')
    axs[1, 2].grid()

args = (1000, 10000)

fig, axs = plt.subplots(2, 3, figsize=(12, 7))
drawPhasePortrait(args)
plt.show()
