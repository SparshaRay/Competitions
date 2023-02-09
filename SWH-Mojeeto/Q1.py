import matplotlib.pyplot as plt
year = []
latitude = []
path = input('Path to file - ')
f = open(path, 'r').read().split('\n')[1:-1]
for line in f :
    l = line.split()
    for i in range(round(float(l[7]))) :
        year.append(l[0])
        latitude.append(l[5])
plt.hexbin(year, latitude, gridsize=(103, 50), cmap='inferno')
plt.show()