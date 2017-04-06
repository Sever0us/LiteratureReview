from matplotlib import pyplot as plt
import numpy as np
from math import tanh


def simple():
    t = np.linspace(0, 4, 100)
    ein = [0.3 * 0.25 * 1368 for x in t]
    eout = [x**4 for x in t]

    fig, ax = plt.subplots(1)

    ax.plot(t, ein, label="Energy absorbed by earth")
    ax.plot(t, eout, label="Energy emitted by earth")

    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.legend()
    plt.title("Simple Energy Balance Model")
    plt.xlabel('Temperature of the Earth $\\left(K\\right)$')
    plt.ylabel('Power desnsity $\\left(\\frac{w}{m^2}\\right)$')

    plt.savefig('img\\constant_albedo.png')


def intermediate():
    t = np.linspace(1, 5, 100)
    ein = []
    eout = []

    for temp in t:
        alpha =  0.21+ 0.2 * tanh((temp - 3)*3)
        ein.append(alpha*0.25 * 1368)
        eout.append(0.6*temp**4)

    fig, ax = plt.subplots(1)

    ax.plot(t, ein, label="Energy absorbed by earth")
    ax.plot(t, eout, label="Energy emitted by earth")

    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.legend()
    plt.title("Greenhouse Model")
    plt.xlabel('Temperature of the Earth $\\left(K\\right)$')
    plt.ylabel('Power desnsity $\\left(\\frac{w}{m^2}\\right)$')

    plt.savefig('img\\greenhouse.png')


if __name__ == "__main__":
    simple()
    intermediate()
