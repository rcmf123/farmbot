import matplotlib.pyplot as plt
import numpy as np
import funcs


def plot_bar_x(x):
    levels = ['All levels','Per level total', 'Level 2', 'Leve 3', 'Level 4', 'Level 5']
    time = []
    
    plt.ion()
    f = plt.figure()
    time.append(funcs.time(0)) #continuous
    time.append(funcs.time(2)+funcs.time(3)+funcs.time(4)+funcs.time(5)) #total of per level
    time.append(funcs.time(2))
    time.append(funcs.time(3))
    time.append(funcs.time(4))
    time.append(funcs.time(5))
    
    # this is for graphing purpose
    
    index = np.arange(len(levels))
    plt.bar(index, time)
    plt.xlabel('Levels', fontsize=10)
    plt.ylabel('Estimated flight time', fontsize=10)
    plt.xticks(index, levels, fontsize=5, rotation=30)
    plt.title('Time comparison for each levels')

    plt.savefig('results\graph.png')
    plt.ioff()
    if x == 1:
        plt.show()
    plt.close()
    print(time)


