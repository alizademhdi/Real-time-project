from schedulers.MRSP import simulate_mrsp
from schedulers.MSRP import simulate_msrp
from tools.task_generator import generate_tasks, generate_resources


def evaluate(tasks, resources, num_processors, protocol, end_time):
    if protocol == 'MSRP':
        simulate_msrp(tasks, resources, num_processors, end_time)
    elif protocol == 'MRSP':
        simulate_mrsp(tasks, resources, num_processors, end_time)
    
    total_utilization = sum(t['wcet'] / t['period'] for t in tasks) / num_processors
    print(f'Protocol: {protocol}, Utilization: {total_utilization}')

if __name__ == '__main__':
    num_tasks = 10
    num_resources = 2
    U_total = 0.8
    min_period = 10
    max_period = 100
    num_processors = 2
    end_time = 1000
    tasks = generate_tasks(num_tasks, U_total, min_period, max_period)
    resources = generate_resources(tasks, num_resources)

    evaluate(tasks, resources, num_processors, 'MSRP', end_time)
