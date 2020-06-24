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
    import numpy as np

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
