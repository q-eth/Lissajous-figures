import numpy as np
import matplotlib.pyplot as plt

def lissajous(a, b, w1, w2, delta, t):
    x = a * np.cos(w1 * t)
    y = b * np.cos(w2 * t + delta)
    return x, y

def plot_lissajous_figures():
    t = np.linspace(0, 2 * np.pi, 1000)
    
    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    axs = axs.flatten()
    
    deltas = [0, np.pi, np.pi/2, 3 * np.pi/2, np.pi/4]
    labels = ["Прямая", "Прямая c обратным наклоном", "Окружность", "Эллипс", "Общий график"]
    colors = ['#FF0000', '#00FF00', '#0000FF', '#BED600', '#FF0000']
    
    for i in range(4):
        if labels[i] != "Эллипс":
            a, b = (1, 1) 
        else:
            a, b = (1, 0.5)
        x, y = lissajous(a, b, 1, 1, deltas[i], t)
        axs[i].plot(x, y, color=colors[i])
        axs[i].set_title(labels[i])
        axs[i].grid()
        axs[i].set_xlim(-2, 2)
        axs[i].set_ylim(-2, 2)
    
    for i, delta in enumerate(np.linspace(0, 2 * np.pi, 5)):
        if labels[i] != "Эллипс":
            a, b = (1, 1) 
        else:
            a, b = (1, 0.5)
        x, y = lissajous(a, b, 1, 1, delta, t)
        axs[4].plot(x, y, color=colors[i], label=f'delta = {round(delta, 2)}')
    axs[4].set_title(labels[4])
    axs[4].legend()
    axs[4].grid()
    axs[4].set_xlim(-2, 2)
    axs[4].set_ylim(-2, 2)
    
    plt.tight_layout()
    plt.show()

plot_lissajous_figures()