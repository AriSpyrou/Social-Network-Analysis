import networkx as nx
import matplotlib.pyplot as plt

N = 12


def min_max():
    try:
        f = open('min_max.txt')
        f = f.read().split(',')
        max = int(f[0])
        min = int(f[1])
    except FileNotFoundError:
        with open('sx-stackoverflow.txt') as f:
            line = f.readline()
            max = int(line.split(' ')[2].replace('/n', ''))
            min = int(line.split(' ')[2].replace('/n', ''))
            for line in f:
                line = line.split(' ')
                line[2] = int(line[2].replace('/n', ''))
                if line[2] > max:
                    max = line[2]
                elif line[2] < min:
                    min = line[2]
        print('Max is: ', str(max),
              '\nMin is: ', str(min))
        f = open('min_max.txt', 'w')
        f.write(str(max) + ',' + str(min))
    return max, min


def graph(t):
    G = nx.DiGraph()
    with open('sx-stackoverflow.txt') as f:
        for line in f:
            if int(line.split(' ')[2].replace('\n', '')) < qN[t][1]:
                G.add_node(line[0])
                G.add_edge(line[0], line[1])
    nx.draw(G)
    plt.show()


max_time, min_time = min_max()
dt = max_time - min_time
tN = []
qN = []
dT = dt / N
for j in range(N):
    tN.append(int(min_time + j * dT))
for j in range(len(tN) - 1):
    qN.append([tN[j], tN[j+1]])

for i in range(N - 1):
    graph(i)
