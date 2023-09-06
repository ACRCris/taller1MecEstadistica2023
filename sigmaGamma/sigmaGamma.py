import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

sigmaX = np.asarray([4.74444,3.54046, 2.46086,1.73788,1.21989])
gammaResorte = np.asarray([4/60000, 4/30000, 4/15000, 4/7500, 4/3750])
k=1
m=1



slope, intercept, r, p, se = stats.linregress(np.log(gammaResorte), np.log(sigmaX**2))

print(slope, intercept, r, p, se)

def plot_sigmae2Gamma(sigmaX, gammaResorte, slope, intercept, r):
    fig, ax = plt.subplots(1,2, figsize=(10,5))
    #sigma cuadrado
    x= np.linspace(0.000065, 0.00115, 100)
    sigmaX2 = sigmaX**2
    ax[0].plot(gammaResorte, sigmaX2,'o', markersize=3)
    ax[0].plot(x, np.exp(intercept)*x**slope)
    ax[0].set_ylabel(r'$\sigma^2$')
    ax[0].set_xlabel(r'$\gamma$')
    ax[0].set_title(r'$\gamma$ vs $\sigma^2$')
    ax[0].text(0.00012, 1.5, r'$\ln(\sigma^2) = {%.2f}\ln(\gamma) {%.2f}$'%(slope, intercept), fontsize=10)

    ax[0].legend(['Datos', 'Ajuste'])
    ##Equation

    ax[0].set_xscale('log')
    ax[0].set_yscale('log')


    sigmaX2 = sigmaX**2
    ax[1].plot(gammaResorte, sigmaX2,'o', markersize=3)
    ax[1].plot(x, np.exp(intercept)*x**slope)
    ax[1].set_ylabel(r'$\sigma^2$')
    ax[1].set_xlabel(r'$\gamma$')
    ax[1].set_title(r'$\gamma$ vs $\sigma^2$')
    ax[1].text(0.00012, 1.5, r'$\sigma^2 = \gamma^{%.2f}e^{%.2f}$'%(slope, intercept), fontsize=10)

    ax[1].legend(['Datos', 'Ajuste'])
    fig.savefig('sigma2Gamma.png', dpi=600)
    ##Equation



    
    plt.show()


    
    
plot_sigmae2Gamma(sigmaX, gammaResorte, slope, intercept, r)