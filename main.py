from schedulers.MRSP import simulate_mrsp
from schedulers.MSRP import simulate_msrp
from tools.task_generator import generate_tasks


def evaluate(tasks, num_processors, protocol, end_time):
    if protocol == 'MSRP':
        simulate_msrp(tasks, num_processors, end_time)
    elif protocol == 'MRSP':
        simulate_mrsp(tasks, num_processors, end_time)
    
    total_utilization = sum(t['wcet'] / t['period'] for t in tasks) / num_processors
    print(f'Protocol: {protocol}, Utilization: {total_utilization}')

if __name__ == '__main__':
    tasks = generate_tasks(10, 1, 10, 1020)
    evaluate(tasks, 2, 'MRSP', 1000)