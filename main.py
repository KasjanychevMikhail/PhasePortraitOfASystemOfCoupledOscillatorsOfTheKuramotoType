import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def rhs(s, v):
    return [0.5 + 0.25 * (-2 * np.cos(v[0] - v[0]) - 2 * np.cos(2 * v[0] - v[1]) - np.cos(3 * v[0] - v[2]) - 0.88 * np.cos(4 * v[0] - v[3])),
            0.2 + 0.25 * (-2 * np.cos(v[1] - v[0]) - 2 * np.cos(2 * v[1] - v[1]) - np.cos(3 * v[1] - v[2]) - 0.88 * np.cos(4 * v[1] - v[3])),
            0.7 + 0.25 * (-2 * np.cos(v[2] - v[0]) - 2 * np.cos(2 * v[2] - v[1]) - np.cos(3 * v[2] - v[2]) - 0.88 * np.cos(4 * v[2] - v[3])),
            0.9 + 0.25 * (-2 * np.cos(v[3] - v[0]) - 2 * np.cos(2 * v[3] - v[1]) - np.cos(3 * v[3] - v[2]) - 0.88 * np.cos(4 * v[3] - v[3]))]

def drawPhasePortrait(args, deltaY0=1, startY0=0, stopY0=5):
    for y0 in range(startY0, stopY0, deltaY0):
        for y10 in range(startY0, stopY0, deltaY0):
            for y20 in range(startY0, stopY0, deltaY0):
                for y30 in range(startY0, stopY0, deltaY0):
                    res = solve_ivp(rhs, (args[0], args[1]), [y0, y10, y20, y30])
                    axs[0, 0].plot(res.y[0].T, res.y[1].T, 'b')
                    axs[0, 1].plot(res.y[0].T, res.y[2].T, 'b')
                    axs[0, 2].plot(res.y[0].T, res.y[3].T, 'b')
                    axs[1, 0].plot(res.y[1].T, res.y[2].T, 'b')
                    axs[1, 1].plot(res.y[1].T, res.y[3].T, 'b')
                    axs[1, 2].plot(res.y[2].T, res.y[3].T, 'b')
    axs[0, 0].set(xlabel='theta1')
    axs[0, 0].set(ylabel='theta2')
    axs[0, 0].grid()
    axs[0, 1].set(xlabel='theta1')
    axs[0, 1].set(ylabel='theta3')
    axs[0, 1].grid()
    axs[0, 2].set(xlabel='theta1')
    axs[0, 2].set(ylabel='theta4')
    axs[0, 2].grid()
    axs[1, 0].set(xlabel='theta2')
    axs[1, 0].set(ylabel='theta3')
    axs[1, 0].grid()
    axs[1, 1].set(xlabel='theta2')
    axs[1, 1].set(ylabel='theta4')
    axs[1, 1].grid()
    axs[1, 2].set(xlabel='theta3')
    axs[1, 2].set(ylabel='theta4')
    axs[1, 2].grid()

args = (-15, 15)
fig, axs = plt.subplots(2, 3, figsize=(12, 7))
drawPhasePortrait(args)
plt.show()
