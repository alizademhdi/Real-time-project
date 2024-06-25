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

def generate_tasks(n, U_total, min_period, max_period, num_resources=2, num_critical_sections=2, max_preemption_level=3):
    utilizations = uunifast(n, U_total)
    tasks = []
    for i, u in enumerate(utilizations):
        period = random.randint(min_period, max_period)
        wcet = int(u * period) + 1
        deadline = period
        number_of_critical_sections = random.randint(1, num_critical_sections)
        preemtaion_level = random.randint(1, max_preemption_level)
        criticality = []
        for _ in range(number_of_critical_sections):
            critical_section_length = random.randint(1, 2)
            critical_section_start = random.randint(0, wcet-1)
            critical_section_end = random.randint(critical_section_start, min(wcet, critical_section_start + critical_section_length))
            critical_resource = random.randint(0, num_resources - 1)
            criticality.append({
                'start': critical_section_start, 'end': critical_section_end, 'resource': critical_resource
            })
        tasks.append({
            'id': i,
            'period': period,
            'wcet': wcet,
            'start_time': None,
            'deadline': deadline,
            'preemption_level': preemtaion_level,
            'criticality': criticality,
            'remaining_time': wcet,
            'arrival': 0,
            'utilization': u,
            'blocking': False,
        })
    return tasks

def print_tasks(tasks):
    for t in tasks:
        print(t)