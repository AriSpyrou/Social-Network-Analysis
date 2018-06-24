import signal
import sys

N_Par = 12


def signal_handler(signal, frame):
    print('Max is: ', str(max_time), 'Min is: ', str(min_time))
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
with open('sx-stackoverflow.txt') as f:
    line = f.readline()
    max_time = int(line.split(' ')[2].replace('/n', ''))
    min_time = int(line.split(' ')[2].replace('/n', ''))
    for line in f:
        line = int(line.split(' ')[2].replace('/n', ''))
        if line > max_time:
            max_time = line
        elif line < min_time:
            min_time = line
print('Max is: ', str(max_time), '\nMin is: ', str(min_time))

dt = max_time - min_time
tN = []
qN = []
dT = dt / N_Par
for j in range(N_Par):
    tN.append(int(min_time + j * dT))
for j in range(len(tN) - 1):
    qN.append([tN[j], tN[j+1]])
