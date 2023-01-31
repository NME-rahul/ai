import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create():
    fig, ax = plt.subplots()
    x = np.linspace(0, 1000, 10)
    line, = plt.plot(x, np.sin(x))

    def animator(i):
    	line.set_ydata(np.sin(x+i/50))
    	return line,
	
    ani = animation.FuncAnimation(fig, animator, interval=20, blit=True, save_count=50)

    plt.show()
