import matplotlib.pyplot as plt

def draw(avg, name):
    run = [i for i in range(1, 11)]

    plt.plot(run, avg )
    plt.xlabel("run")
    plt.ylabel("average schedule-ables")
    plt.yticks(range(60 ,120, 10))
    plt.title(f'number of proccesor = {name}')
    plt.savefig(f'{name}.png')
    