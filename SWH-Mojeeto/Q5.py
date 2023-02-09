import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pos1 = np.array([float(input('x coordinate of first body - ')), float(input('y coordinate of first body - '))])
pos2 = np.array([float(input('x coordinate of second body - ')), float(input('y coordinate of second body - '))])
vel1 = np.array([float(input('x velocity of first body - ')), float(input('y velocity of first body - '))])
vel2 = np.array([float(input('x velocity of second body - ')), float(input('y velocity of second body - '))])

a, b = float(input('length of major axis - ')), float(input('length of minor axis - '))

m1, m2 = float(input('mass of first body - ')), float(input('mass of second body - '))
k = float(input('value of k - '))

timestep = 0.001

fig = plt.figure()
plt.xlim([-a, a])
plt.ylim([-b, b])
plot, = plt.plot([], [], 'r.')

def update(frame):

    global pos1, pos2, vel1, vel2

    theta1 = np.arctan((a*pos1[1])/(b*pos1[0]))
    if (abs(b*np.sin(theta1) - pos1[1]) > 0.0001) or (abs(a*np.cos(theta1) - pos1[0]) > 0.0001) : 
        theta1 = theta1 + np.pi
    tan1 = np.array([-a*np.sin(theta1), b*np.cos(theta1)])

    theta2 = np.arctan((a*pos2[1])/(b*pos2[0]))
    if (abs(b*np.sin(theta2) - pos2[1]) > 0.0001) or (abs(a*np.cos(theta2) - pos2[0]) > 0.0001) : 
        theta2 = theta2 + np.pi
    tan2 = np.array([-a*np.sin(theta2), b*np.cos(theta2)])

    f1 = (-4 * k * (pos1 - pos2) * (np.linalg.norm(pos1 - pos2))**2) 
    f2 = (-4 * k * (pos2 - pos1) * (np.linalg.norm(pos2 - pos1))**2)

    f1comp = tan1 * np.dot(f1, tan1) / (np.linalg.norm(tan1) ** 2 )
    f2comp = tan2 * np.dot(f2, tan2) / (np.linalg.norm(tan2) ** 2 )

    a1 = f1comp/m1
    a2 = f2comp/m2

    vel1 = vel1 + a1 * timestep
    vel2 = vel2 + a2 * timestep

    pos1 = pos1 + vel1 * timestep
    pos2 = pos2 + vel2 * timestep

    theta1 = np.arctan((a*pos1[1])/(b*pos1[0]))
    if (abs(b*np.sin(theta1) - pos1[1]) > 0.00001) or (abs(a*np.cos(theta1) - pos1[0]) > 0.00001) : 
        theta1 = theta1 + np.pi

    theta2 = np.arctan((a*pos2[1])/(b*pos2[0]))
    if (abs(b*np.sin(theta2) - pos2[1]) > 0.00001) or (abs(a*np.cos(theta2) - pos2[0]) > 0.00001) : 
        theta2 = theta2 + np.pi

    pos1 = np.array([a*np.cos(theta1), b*np.sin(theta1)])
    pos2 = np.array([a*np.cos(theta2), b*np.sin(theta2)])


    x = [pos1[0], pos2[0]]
    y = [pos1[1], pos2[1]]

    plot.set_data(x, y)
    return plot,

ani = animation.FuncAnimation(fig, update, interval=1000/30)
plt.show()