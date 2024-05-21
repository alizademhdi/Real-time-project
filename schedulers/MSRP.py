from tools.scheduling import*

def simulate_msrp(tasks, num_processors, end_time):
    processors = wfd_mapping(tasks, num_processors)
    time = 0
    while time < end_time:
        for p in processors:
            task = edf_schedule(p, time)
            if task:
                for t in p:
                    if t != task:
                        t['blocked'] = True
                
                task['remaining_time'] -= 1
                if task['remaining_time'] == 0:
                    task['next_release'] += task['period']
                    task['remaining_time'] = task['wcet']
                
                for t in p:
                    t['blocked'] = False
        
        time += 1