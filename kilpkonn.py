import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-7, 8, 1) 
y=-3/49*(x**2)+8
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-7, 8, 1)
y=4/49*(x**2)+1
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-6.9, -1, 1)
y=-0.75*((x+4)**2)+11
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(2, 7.01, 0.5)
y=-0.75*(x-4)**2+11
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-5.8, -1.8, 1)
y=-((x+4)**2)+9
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(2.8, 6.8, 1)
y=-((x-4)**2)+9
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-4, 5, 1)
y=4/9*(x**2)-5
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-5.2,5.8,0.5)
y=4/9*x**2-9
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-7, -2, 1)
y=-1/16*((x+3)**2)-6
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(2.8, 8, 1)
y=-1/16*((x-3)**2)-6
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-7, 1, 1)
y=1/9*((x+4)**2)-11
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(0, 8, 1)
y=1/9*((x-4)**2)-11
plt.plot(x,y, color='green', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-7, -3.5, 1)
y=-((x+5)**2)
plt.plot(x,y, color='red', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(4.5, 7.6, 0.8)
y=-((x-5)**2)
plt.plot(x,y, color='red', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")
x=np.arange(-3, 4, 1)
y=2/9*(x**2)+2
plt.plot(x,y, color='red', linestyle='-', marker='D',
    markersize=5, label="Joonisejoon")



plt.figure(facecolor='lightblue')
plt.title("Kilpkonn")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)
plt.show()

