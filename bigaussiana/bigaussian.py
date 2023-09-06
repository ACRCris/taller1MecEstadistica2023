import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def bigaussiana(x, y, mu1, mu2, sigma1, sigma2, rho):
    xy = np.column_stack([x.flat, y.flat])
    z = multivariate_normal.pdf(xy, mean=[mu1, mu2], cov=[[sigma1**2, rho*sigma1*sigma2], [rho*sigma1*sigma2, sigma2**2]])
    z = z.reshape(x.shape)
    return z

def plot_bigaussiana(x, y, z):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x,y, z, cmap='viridis', linewidth=0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    

def main():
    mu1 = 0
    mu2 = 0
    sigma1 = 2
    sigma2 = 2
    rho = 0
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    print(x)
    print(y)
    z = bigaussiana(x, y, mu1, mu2, sigma1, sigma2, rho)
    plot_bigaussiana(x, y, z)

main()

    

