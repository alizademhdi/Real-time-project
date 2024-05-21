import random

def uunifast(n, U_total):
    utilizations = []
    sum_U = U_total
    for i in range(1, n):
        next_sum_U = sum_U * (random.random() ** (1 / (n - i)))
        utilizations.append(sum_U - next_sum_U)
        sum_U = next_sum_U
    utilizations.append(sum_U)
    return utilizations

def generate_tasks(n, U_total, min_period, max_period):
    utilizations = uunifast(n, U_total)
    tasks = []
    for i, u in enumerate(utilizations):
        period = random.randint(min_period, max_period)
        wcet = u * period
        deadline = period
        tasks.append({
            'id': i, 'period': period, 'wcet': wcet, 'deadline': deadline,
            'remaining_time': wcet, 'next_release': 0, 'processor': -1, 'blocked': False
        })
    return tasks