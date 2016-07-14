#!/usr/bin/env python

from math import ceil, floor
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

DEBUG = False

profile = [
    [100.00000, 0.00000],   # 0
    [99.66700,  -0.06100],
    [98.72500,  -0.25500],
    [97.27500,  -0.55500],
    [95.35700,  -0.88100],
    [92.95200,  -1.19000],  # 5
    [90.06200,  -1.49300],
    [86.72300,  -1.79300],
    [82.97200,  -2.08800],
    [78.85400,  -2.37200],
    [74.41400,  -2.64300],  # 10
    [69.70200,  -2.89600],
    [64.77300,  -3.12700],
    [59.68100,  -3.33200],
    [54.48300,  -3.50700],
    [49.23900,  -3.64900],  # 15
    [44.00700,  -3.75400],
    [38.84700,  -3.81900],
    [33.81500,  -3.83900],
    [28.96800,  -3.81200],
    [24.36000,  -3.73200],  # 20
    [20.04000,  -3.59700],
    [16.05400,  -3.40400],
    [12.44400,  -3.14900],
    [9.24400,   -2.83300],
    [6.48400,   -2.45500],
    [4.18700,   -2.01800],
    [2.37000,   -1.53000],
    [1.04600,   -1.00200],
    [0.22500,   -0.46800],
    [0.00000,   0.07000],
    [0.36700,   0.69400],
    [1.19600,   1.41100],
    [2.47500,   2.15900],
    [4.19100,   2.90400],
    [6.33000,   3.62000],
    [8.87400,   4.28900],
    [11.80000,  4.89500],
    [15.07900,  5.42400],
    [18.67800,  5.86100],
    [22.55800,  6.19200],
    [26.67700,  6.39600],
    [31.00700,  6.44500],
    [35.52900,  6.32700],
    [40.22400,  6.04200],
    [45.07300,  5.60000],
    [50.05200,  5.02200],
    [55.13800,  4.34600],
    [60.28300,  3.63100],
    [65.41200,  2.92200],
    [70.44700,  2.24900],
    [75.31400,  1.63700],
    [79.93600,  1.10400],
    [84.23900,  0.66300],
    [88.15400,  0.32200],
    [91.61200,  0.08500],
    [94.55200,  -0.05000],
    [96.90700,  -0.09100],
    [98.61900,  -0.06600],
    [99.65400,  -0.02100],
    [100.00000, 0.00000],
]


class TangentInterpolation(object):
    def __init__(self, profile):
        self.profile = tuple(profile)

    @staticmethod
    def _linear_interp(t0, t1, z0, z1):
        a = (z0 - z1) / (t0 - t1)
        b = z0 - a * t0

        if DEBUG:
            print('t0, t1, z0, z1 (%f, %f, %f, %f) --> a, b (%f, %f)' % \
                (t0, t1, z0, z1, a, b))

        return (a, b)

    def __call__(self, t):
        """evaluate the (x, y) values for t in [0 - 1] interval"""
        t = t * (len(self.profile) - 1)

        # find the nearest points
        t0 = ceil(t)
        t1 = floor(t)
        if DEBUG:
            print('t = %f --> t0 = %f, t1 = %f' % (t, t0, t1))

        if int(t0) == int(t1):
            x, y =  self.profile[int(t0)]

        else:
            x0 = profile[int(t0)][0]
            x1 = profile[int(t1)][0]
            a, b = self._linear_interp(t0, t1, x0, x1)
            x = a * t + b

            y0 = profile[int(t0)][1]
            y1 = profile[int(t1)][1]
            a, b = self._linear_interp(t0, t1, y0, y1)
            y = a * t + b

        if DEBUG:
            print('(x, y) = (%f, %f)' % (x, y))
        return (x, y)

#x = np.linspace(-3, 3, 50)
#y = np.exp(-x**2) + 0.1 * np.random.randn(50)
x, y = zip(*profile)
plt.plot(x, y, 'ro', ms=5)

#xs = np.linspace(-3, 3, 1000)
#spl = InterpolatedUnivariateSpline(x, y)
#plt.plot(xs, spl(xs), 'g', lw=3, alpha=0.7)

#tginterp = TangentInterpolation(profile)
#res = [tginterp(t) for t in np.linspace(0, 1, 20)]
#x, y = zip(*res)
#plt.plot(x, y, 'g', lw=3, alpha=0.7)

t = np.linspace(0, 1, len(profile))
x_spl = InterpolatedUnivariateSpline(t, x)
y_spl = InterpolatedUnivariateSpline(t, y)

t = np.linspace(0, 1, 4 * len(profile))
x = [x_spl(_t) for _t in t]
y = [y_spl(_t) for _t in t]

plt.plot(x, y, 'g', lw=3, alpha=0.7)

plt.show()

