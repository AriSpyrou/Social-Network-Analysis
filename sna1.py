import networkx as nx
import matplotlib.pyplot as plt
import collections as col

N_RL = 500

N = 6


def min_max():
    try:
        f = open('min_max' + str(N_RL) + '.txt')
        f = f.read().split(',')
        max = int(f[0])
        min = int(f[1])
    except FileNotFoundError:
        with open('sx-stackoverflow.txt') as f:
            line = f.readline()
            max = int(line.split(' ')[2].replace('\n', ''))
            min = int(line.split(' ')[2].replace('\n', ''))
            for j in range(N_RL):
                line = f.readline().split(' ')
                line[2] = int(line[2].replace('\n', ''))
                if line[2] > max:
                    max = line[2]
                elif line[2] < min:
                    min = line[2]
        print('Max is: ', str(max),
              '\nMin is: ', str(min))
        f = open('min_max' + str(N_RL) + '.txt', 'w')
        f.write(str(max) + ',' + str(min))
    return max, min


def graph(t, centrality='degree'):
    g = nx.DiGraph()
    with open('sx-stackoverflow.txt') as f:
        for j in range(N_RL):
            line = f.readline().split(' ')
            line[2] = int(line[2].replace('\n', ''))
            if line[2] < qN[t][1] or (t == N - 1 and line[2] <= qN[t][1]):
                g.add_node(line[0])
                g.add_edge(line[0], line[1])
    nx.draw_networkx(g, node_size=150, font_size=10)
    plt.show()
    centrality_histogram(g, centrality)


def centrality_histogram(g, c):
    if c == 'degree':
        degree_sequence = sorted([val for key, val in nx.degree_centrality(g).items()])
    elif c == 'in_degree':
        degree_sequence = sorted([val for key, val in nx.in_degree_centrality(g).items()])
    elif c == 'out_degree':
        degree_sequence = sorted([val for key, val in nx.out_degree_centrality(g).items()])
    elif c == 'closeness':
        degree_sequence = sorted([val for key, val in nx.closeness_centrality(g).items()])
    elif c == 'betweenness':
        degree_sequence = sorted([val for key, val in nx.betweenness_centrality(g).items()])
    elif c == 'eigenvector':
        degree_sequence = sorted([val for key, val in nx.eigenvector_centrality(g).items()])
    elif c == 'katz':
        degree_sequence = sorted([val for key, val in nx.katz_centrality(g).items()])
    degree_count = col.Counter(degree_sequence)
    deg, cnt = zip(*degree_count.items())
    plt.bar(deg, cnt, width=0.01, color='b')
    plt.title('Degree Histogram')
    plt.ylabel('Count')
    plt.xlabel('Degree')
    plt.show()


def graph_star(t):
    if t < N - 1:
        g1 = nx.DiGraph()
        g2 = nx.DiGraph()
        with open('sx-stackoverflow.txt') as f:
            for j in range(N_RL):
                line = f.readline().split(' ')
                line[2] = int(line[2].replace('\n', ''))
                if line[2] < qN[t][1]:
                    g1.add_node(line[0])
                    g1.add_edge(line[0], line[1])
                elif line[2] < qN[t + 1][1]:
                    g2.add_node(line[0])
                    g2.add_edge(line[0], line[1])
        v_star = []
        e1_star = []
        e2_star = []
        for i in g1.nodes:
            for j in g2.nodes:
                if i == j:
                    v_star.append(i)
                    break
        for i in g1.edges:
            found1 = False
            found2 = False
            for j in v_star:
                if i[0] == j:
                    found1 = True
                elif i[1] == j:
                    found2 = True
            if found1 and found2:
                e1_star.append(i)

        for i in g2.edges:
            found1 = False
            found2 = False
            for j in v_star:
                if i[0] == j:
                    found1 = True
                elif i[1] == j:
                    found2 = True
            if found1 and found2:
                e2_star.append(i)
        print('t =', t)
        print('V*[t_', t, ',', 't_', t+2, '} = ', v_star)
        print('E*[t_', t, ',', 't_', t+1, '] =', e1_star)
        print('E*[t_', t+1, ',', 't_', t+2, '] =', e2_star)


max_time, min_time = min_max()
dt = max_time - min_time
tN = []
qN = []
dT = dt / N
for j in range(N + 1):
    tN.append(int(min_time + j * dT))
for j in range(len(tN) - 1):
    qN.append([tN[j], tN[j+1]])
del tN

for i in range(N):
    #graph(i, centrality='closeness')
    graph_star(i)
