from schedulers.MRSP import simulate_mrsp
from schedulers.MSRP import simulate_msrp
from tools.task_generator import generate_tasks, print_tasks
from tools.scheduling import edf_schedule, wfd_mapping


def evaluate(tasks, resources, num_processors, protocol, end_time):
    if protocol == 'MSRP':
        simulate_msrp(tasks, resources, num_processors, end_time)
    elif protocol == 'MRSP':
        simulate_mrsp(tasks, resources, num_processors, end_time)

if __name__ == '__main__':
    num_tasks = 10
    num_resources = 2
    processors_utilization = [0.25, 0.25]
    U_total = sum(processors_utilization)
    min_period = 10
    max_period = 100
    num_processors = 2
    end_time = 1000
    tasks = generate_tasks(num_tasks, U_total, min_period, max_period, num_resources)
    processors = wfd_mapping(tasks, num_processors)
    print_tasks(tasks)
    print(processors[0])
