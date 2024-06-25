from schedulers.MRSP import simulate_mrsp
from schedulers.MSRP import simulate_msrp
from tools.task_generator import generate_tasks, print_tasks
from tools.scheduling import wfd_mapping, calculate_ceilings
from math import lcm
from functools import reduce
from tools.plot import draw
from sample import sample_tasks


def evaluate(processors, num_resources, protocol, end_time, ceilings):
    if protocol == 'MSRP':
        scheduleable, non_scheduleable = simulate_msrp(processors, num_resources, end_time, ceilings)
    elif protocol == 'MRSP':
        scheduleable, non_scheduleable = simulate_mrsp(processors, num_resources, end_time, ceilings)
    return scheduleable, non_scheduleable

def calculate_huperperiod(tasks):
    return reduce(lcm, [t['period'] for t in tasks])

if __name__ == '__main__':
    num_tasks = 100
    num_resources = 2
    processors_utilization = [0.25, 0.25]
    U_total = sum(processors_utilization)
    min_period = 15
    max_period = 25
    num_processors = 2
    max_premption_level = 3
    max_critical_sections = 2
    num_run = 1
    avg = []
    for _ in range(num_run):
        tasks = generate_tasks(num_tasks, U_total, min_period, max_period, num_resources, max_critical_sections, max_premption_level)
        end_time = 100
        tasks = tasks
        ceilings = calculate_ceilings(tasks, num_resources)
        processors = wfd_mapping(tasks, num_processors)
        print_tasks(tasks)
        print(20 * '-')

        scheduleable, non_scheduleable = evaluate(processors, num_resources, 'MSRP', end_time, ceilings)
        avg.append(scheduleable/(scheduleable+non_scheduleable))
    new_avg = [i * 100 for i in avg]
    print(new_avg)
    draw(new_avg, str(num_processors))
