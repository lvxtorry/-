import matplotlib.pyplot as plt
f = open('20046 (1).dat', 'r')
data = []
for s in f.readlines():
    temp = s.split()
    #станция, год, месяц, день, час, направление ветра, осадки, температуа, влажность
    data.append([temp[0], temp[5], temp[6], temp[7], temp[10], float(temp[39]), float(temp[47]), float(temp[-31]), float(temp[-15])])
print(data[0])

x_range = list(map(int, input().split()))

x = range(len(data[x_range[0]:x_range[1]]))
y = [i[-2] for i in data[x_range[0]:x_range[1]]]


plt.figure(figsize=(7, 7))
plt.subplot(3, 1, 1)
plt.title('Температура')
plt.xlabel('Время')
plt.ylabel('Температура')
plt.grid()
plt.plot(x, y, "g")
plt.show()

plt.subplot(3, 1, 2)
plt.title('График y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y, "orange")

plt.subplot(3, 1, 3)
plt.title('График y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y, "blue")
#plt.show()
