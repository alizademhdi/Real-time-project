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

def generate_tasks(n, U_total, min_period, max_period, num_resources=2, num_critical_sections=3):
    utilizations = uunifast(n, U_total)
    tasks = []
    for i, u in enumerate(utilizations):
        period = random.randint(min_period, max_period)
        wcet = int(u * period) + 1
        deadline = period
        number_of_critical_sections = random.randint(1, num_critical_sections)
        criticality = []
        for _ in range(number_of_critical_sections):
            critical_section_length = random.randint(1, wcet)
            critical_section_start = random.randint(0, period - critical_section_length)
            critical_section_end = critical_section_start + critical_section_length
            critical_resource = random.randint(0, num_resources - 1)
            criticality.append({
                'start': critical_section_start, 'end': critical_section_end, 'resource': critical_resource
            })
        tasks.append({
            'id': i,
            'period': period,
            'wcet': wcet,
            'deadline': deadline,
            'criticality': criticality,
            'remaining_time': wcet,
            'next_release': period,
            'utilization': u,
        })
    return tasks

def print_tasks(tasks):
    for t in tasks:
        print(t)