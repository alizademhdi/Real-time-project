from tools.scheduling import *


def simulate_mrsp(tasks, num_processors, end_time):
    processors = wfd_mapping(tasks, num_processors)
    time = 0
    while time < end_time:
        for p in processors:
            task = edf_schedule(p, time)
            if task:
                task['remaining_time'] -= 1
                if task['remaining_time'] == 0:
                    task['next_release'] += task['period']
                    task['remaining_time'] = task['wcet']
        
        time += 1
