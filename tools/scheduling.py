def edf_schedule(tasks, time):
    ready_tasks = [t for t in tasks if t['arrival'] <= time and t['remaining_time'] > 0]
    if ready_tasks:
        return min(ready_tasks, key=lambda t: t['deadline'])
    return None


def calculate_ceilings(tasks, num_resources):
    ceilings = []
    for r in range(num_resources):
        max_preemption_level = 0
        for t in tasks:
            for c in t['criticality']:
                if c['resource'] == r:
                    max_preemption_level = max(max_preemption_level, t['preemption_level'])
        ceilings.append(max_preemption_level)
    return ceilings

def wfd_mapping(tasks, num_processors):
    processors = [[] for _ in range(num_processors)]
    
    for task in sorted(tasks, key=lambda t: -t['utilization']):
        worst_fit_processor = min(processors, key=lambda p: sum(t['utilization'] for t in p))
        worst_fit_processor.append(task)
        task['processor'] = processors.index(worst_fit_processor)
    return processors