from schedulers.MRSP import simulate_mrsp
from schedulers.MSRP import simulate_msrp
from tools.task_generator import generate_tasks, print_tasks
from tools.scheduling import edf_schedule, wfd_mapping, calculate_ceilings
from math import lcm
from functools import reduce
from sample import sample_tasks
import time


def evaluate(resources, num_processors, protocol, end_time, ceilings):
    if protocol == 'MSRP':
        simulate_msrp(resources, num_processors, end_time, ceilings)
    elif protocol == 'MRSP':
        simulate_mrsp(resources, num_processors, end_time)

def calculate_huperperiod(tasks):
    return reduce(lcm, [t['period'] for t in tasks])

if __name__ == '__main__':
    num_tasks = 10
    num_resources = 2
    processors_utilization = [0.25, 0.25]
    U_total = sum(processors_utilization)
    min_period = 10
    max_period = 20
    num_processors = 2
    max_premption_level = 3
    max_critical_sections = 2
    tasks = generate_tasks(num_tasks, U_total, min_period, max_period, num_resources, max_critical_sections, max_premption_level)
    end_time = calculate_huperperiod(tasks)
    ceilings = calculate_ceilings(tasks, num_resources)
    processors = wfd_mapping(tasks, num_processors)
    print_tasks(tasks)
    print(100 * '-')
    print(end_time)
    time.sleep(5)

    evaluate(processors, num_processors, 'MSRP', end_time, ceilings)
