import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class FiveOscillators:
    def __init__(self, paramW, paramA, paramB, paramR):
        self.paramW = paramW
        self.paramA = paramA
        self.paramB = paramB
        self.paramR = paramR

    def func(self, phi):
        return -np.sin(phi + self.paramA) + self.paramR * np.sin(2 * phi + self.paramB)

    def getFullSystem(self, phis):
        resPhis = [0, 0, 0, 0, 0]
        for i in range(5):
            tmp = self.paramW
            for j in range(5):
                tmp += 0.20 * self.func(phis[i] - phis[j])
            resPhis[i] = tmp
        return resPhis

    def getReducedSystem(self, t, gammas):
        gammas = list(gammas)
        phis = gammas + [0.]
        resPhi = self.getFullSystem(phis)
        resGamma = [0, 0, 0, 0, 0]
        for i in range(5):
            resGamma[i] = resPhi[i] - resPhi[4]
        return resGamma[:-1]

    def getParams(self):
        return[self.paramW, self.paramA, self.paramB, self.paramR]

    def drawPhasePortrait(self, args):
        res = solve_ivp(self.getReducedSystem, (args[0], args[1]), [3.6, 1.7, 1.2, -0.2],
                        t_eval=np.linspace(0, 10000, 20000))
        axs[0, 0].plot(res.y[0].T[8000:10000], res.y[1].T[8000:10000], 'b')
        axs[0, 1].plot(res.y[0].T[8000:10000], res.y[2].T[8000:10000], 'b')
        axs[0, 2].plot(res.y[0].T[8000:10000], res.y[3].T[8000:10000], 'b')
        axs[1, 0].plot(res.y[1].T[8000:10000], res.y[2].T[8000:10000], 'b')
        axs[1, 1].plot(res.y[1].T[8000:10000], res.y[3].T[8000:10000], 'b')
        axs[1, 2].plot(res.y[2].T[8000:10000], res.y[3].T[8000:10000], 'b')

        axs[0, 0].set(xlabel='gamma1')
        axs[0, 0].set(ylabel='gamma2')
        axs[0, 0].grid()
        axs[0, 1].set(xlabel='gamma1')
        axs[0, 1].set(ylabel='gamma3')
        axs[0, 1].grid()
        axs[0, 2].set(xlabel='gamma1')
        axs[0, 2].set(ylabel='gamma4')
        axs[0, 2].grid()
        axs[1, 0].set(xlabel='gamma2')
        axs[1, 0].set(ylabel='gamma3')
        axs[1, 0].grid()
        axs[1, 1].set(xlabel='gamma2')
        axs[1, 1].set(ylabel='gamma4')
        axs[1, 1].grid()
        axs[1, 2].set(xlabel='gamma3')
        axs[1, 2].set(ylabel='gamma4')
        axs[1, 2].grid()

args = (0, 10000)

fig, axs = plt.subplots(2, 3, figsize=(12, 7))
sys = FiveOscillators(1, 1.6, -1.58, 0.2)
sys.drawPhasePortrait(args)
plt.show()
