import matplotlib as plt

def draw(avg, name):
    run = [i for i in range(1, 11)]

    plt.plot(avg, run)
    plt.xlabel("run")
    plt.ylabel("average schedule-ables")
    plt.title("number of proccesor = 2")
    plt.savefig(f'{name}.png')

