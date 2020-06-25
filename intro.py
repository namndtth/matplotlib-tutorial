from matplotlib import pyplot as plt
import numpy as np

def plotY():
    # if provide a single array, 
    # matplotlib assumes it is a sequence of y values
    # and automatically generates the x values
    plt.plot([1, 2, 3, 4])
    plt.ylabel("some numbers")
    plt.show()

def plotXY():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.show()

def format():
    # 3rd argument which is format string that indicates color and line type.
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
    plt.axis([0, 6, 0, 20])
    plt.show()

def matplotlib_with_numpy():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()

def plot_with_keywords():
    data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()

def plot_with_mutiple_figures_and_axes():
    def f(t):
        return np.exp(-t) * np.cos(2 * np.pi* t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.figure(2)
    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

def plot_with_text():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

    plt.xlabel("Smarts")
    plt.ylabel("Probability")
    plt.title("Histogram of IQ")
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()

def annotating_text():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)
    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.ylim(-2, 2)
    plt.show()

def nonlinear_axes():
    # Change the scale of an axis:
    #plt.xscale("log")

    # For reproducibility
    np.random.seed(19680801)

    y = np.random.normal(loc=0.5, scale=0.4, size=1000)

    y = y[(y >0) & (y < 1)]
    y.sort()

    x = np.arange(len(y))

    plt.figure()

    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)

    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)

    # symmetric log
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)

    
    # logit
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)
    #adjust subplots
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
    plt.show()
if __name__ == "__main__":
    nonlinear_axes()