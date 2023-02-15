import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MohrsCircle:
    """Takes Stress Values and calculates various components of those stresses
    as well as plots some of those components and properties
    """

    def __init__(self, sigmax, sigmay, tauxy, units):
        self.sigmax = sigmax
        self.sigmay = sigmay
        self.tauxy = tauxy
        self.units = units

    def sigma_avg(self):
        return round((self.sigmax + self.sigmay) / 2, 2)

    def radius(self):
        return round(math.sqrt(((self.sigmax - self.sigmay) / 2) ** 2 + self.tauxy ** 2), 2)

    def taumax(self):
        return self.radius()

    def sigma_1(self):
        return round(self.sigma_avg() + self.radius(), 2)

    def sigma_2(self):
        return round(self.sigma_avg() - self.radius(), 2)

    def angle(self):
        if self.sigmay == self.sigma_avg():
            return 0
        else:
            return math.fabs(round(math.degrees(math.atan(self.tauxy / (self.sigma_avg() - self.sigmay))), 2))

    # Creates plot of data
    def circle_plot(self, angle=90):
        # Creating sigma, tau prime based on rotated angle.
        sigmax_prime = round((self.sigmax + self.sigmay) / 2 + (self.sigmax - self.sigmay) / 2 * (
            math.cos(2 * math.radians(angle))) + self.tauxy * math.sin(2 * math.radians(angle)), 2)
        sigmay_prime = round((self.sigmax + self.sigmay) / 2 - (self.sigmax - self.sigmay) / 2 * (
            math.cos(2 * math.radians(angle))) - self.tauxy * math.sin(2 * math.radians(angle)), 2)
        tauxy_prime = round(-(self.sigmax - self.sigmay) / 2 * math.sin(2 * math.radians(angle)) + self.tauxy * (
            math.cos(2 * math.radians(angle))), 2)

        radians = (np.linspace(0, 360, 361)) * math.pi / 180
        sigma_points = self.sigma_avg() + self.radius() * np.cos(radians)
        tau_points = self.radius() * np.sin(radians)

        fig = plt.figure(figsize=[7, 7], constrained_layout=True)
        # Plots points of relevant data
        plt.plot(sigma_points, tau_points)
        plt.plot([self.sigma_avg(), sigmax_prime, sigmax_prime, self.sigma_avg()], [0, 0, tauxy_prime, 0], 'bo-')
        plt.plot([self.sigma_avg(), sigmay_prime, sigmay_prime, self.sigma_avg()], [0, 0, -tauxy_prime, 0], 'bo-')
        plt.plot(self.sigma_1(), 0, color='r')
        plt.plot(self.sigma_2(), 0)

        # Puts text on important points
        plt.text(sigmax_prime, tauxy_prime, f'{sigmax_prime}, {tauxy_prime}', verticalalignment='bottom',
                 horizontalalignment='center', color='r',weight=1000)

        plt.text(sigmay_prime, -tauxy_prime, f'{sigmay_prime}, {-tauxy_prime}', verticalalignment='bottom',
                 horizontalalignment='center', color='r', weight=1000)

        plt.text(self.sigma_avg(), 0, self.sigma_avg(), weight=1000, color='r')

        # Misc. chart edits
        plt.grid()
        plt.title("Mohr's Circle")
        plt.xlabel(f'σ ({self.units})')
        plt.ylabel(f'τ ({self.units})')
        plt.gca().invert_yaxis()
        plt.legend(
            [f'Taumax: {self.taumax()}\nSigma1: {self.sigma_1()}\nSigma2: {self.sigma_2()}\nAngle:{self.angle()}°'],
            bbox_to_anchor=(0.68, 1.155), loc='upper left', ncol=1, fontsize=6, prop=dict(weight='bold'))
        plt.close()
        return fig




# Defines User Inuts
if __name__ == '__main__':
    # sigmax = float(input('Enter Sigma X: '))
    # sigmay = float(input('Enter Sigma Y: '))
    # tauxy = float(input('Enter TauXY: '))
    # units = input('Enter unit type: ')
    m1 = MohrsCircle(-100, 100, 200, units='Kpa')
    m1.circle_plot()
    print('Plotting...')
