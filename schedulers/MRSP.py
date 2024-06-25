from tools.scheduling import *


def simulate_mrsp(tasks, resources, num_processors, end_time):
    processors = wfd_mapping(tasks, num_processors)
    time = 0
    while time < end_time:
        for p in processors:
            pass
        
        time += 1
