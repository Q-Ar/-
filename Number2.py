import matplotlib.pyplot as plt


def graf():
    xy = [[1.5, 2.25, 3, 4.75, 5.5, 6.25, 7], [5.62, 8.45, 8.93, 6.1, 3.1, 1.3, -2.12]], float
    x = xy[0][0]
    y = xy[0][1]
    plt.plot(x, y, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
    plt.legend()
    plt.grid(True)
    plt.show()
    return

