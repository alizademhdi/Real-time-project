def edf_schedule(tasks, time):
    ready_tasks = [t for t in tasks if t['next_release'] <= time and t['remaining_time'] > 0 and not t['blocked']]
    if ready_tasks:
        return min(ready_tasks, key=lambda t: t['deadline'])
    return None

def wfd_mapping(tasks, num_processors):
    processors = [[] for _ in range(num_processors)]
    for task in sorted(tasks, key=lambda t: -t['wcet']):
        worst_fit_processor = min(processors, key=lambda p: sum(t['wcet'] for t in p))
        worst_fit_processor.append(task)
        task['processor'] = processors.index(worst_fit_processor)
    return processors