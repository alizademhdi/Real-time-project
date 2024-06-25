from tools.scheduling import*

def edf_schedule_order(tasks, time):
    ready_tasks = [t for t in tasks if t['arrival'] <= time and t['remaining_time'] > 0]
    if ready_tasks:
        sorted(ready_tasks, key= lambda t: t['deadline'])
        return ready_tasks
    return None

def check_deadlines(processors, time):
    failed = []
    for p in processors:
        for t in p:
            if t['arrival'] <= time and t['remaining_time'] > 0:
                if t['deadline'] < time:
                    print('Task {} missed deadline'.format(t['id']))
                    failed.append(t)
    if len(failed)!=0:
        return True, failed
    return False, None

def simulate_mrsp(processors, num_resources, end_time, ceilings):
    num_schedulable = 0
    num_non_scheduleable = 0
    time = 0
    resources_status = num_resources * [None]
    pi = 0
    current_task = len(processors) * [None]

    while time < end_time:
        print(10*'-')
        print('Time: {}'.format(time))

        for i, p in enumerate(processors):
            if current_task[i] is None:
                continue
            reset = len(current_task[i]['criticality']) * [False]
            for c in current_task[i]['criticality']:
                if c['end'] < task['wcet'] - task['remaining_time']:
                    if resources_status[c['resource']] == current_task[i]['id']:
                        reset[c['resource']] = True
            for c in current_task[i]['criticality']:
                if c['start'] <= task['wcet'] - task['remaining_time'] < c['end']:
                    if resources_status[c['resource']] == current_task[i]['id']:
                        reset[c['resource']] = False
            
            for i in range(len(reset)):
                if reset[i]:
                    resources_status[i] = None
                    
                        
        for i, p in enumerate(processors):
            tasks = edf_schedule_order(p, time)
            
            if tasks is None:
                continue

            for task in tasks:
                blocked = False
                for c in task['criticality']:
                    if c['start'] <= task['wcet'] - task['remaining_time'] < c['end']:
                        if resources_status[c['resource']] is not None and  resources_status[c['resource']] != task['id']:
                            blocked = True
                            task['blocking'] = True
                            break 
                if blocked: 
                    continue 
                if current_task[i] is None:
                    current_task[i] = task
                elif task['id'] != current_task[i]['id']:
                    if task['preemption_level'] > pi:
                        current_task[i] = task
                if current_task[i]['blocking']:
                    current_task[i] = task
                if current_task[i] is None:
                    continue
                current_task[i]['blocking'] = False
                for c in current_task[i]['criticality']:
                    if c['end'] < current_task[i]['wcet'] - current_task[i]['remaining_time']:
                        if resources_status[c['resource']] == current_task[i]['id']:
                            resources_status[c['resource']] = None
            
                for c in current_task[i]['criticality']:
                    if c['start'] <= current_task[i]['wcet'] - current_task[i]['remaining_time'] < c['end']:
                        resources_status[c['resource']] = current_task[i]['id']
                        print('Task {} is using resource {} on proceccor {}'.format(current_task[i]['id'], c['resource'], current_task[i]['processor']))
                
                current_task[i]['remaining_time'] -= 1
                print('Task {} is running on proceccor {}'.format(current_task[i]['id'], current_task[i]['processor']))

                if current_task[i]['remaining_time'] == 0:
                    for c in current_task[i]['criticality']:
                        if resources_status[c['resource']] == current_task[i]['id']:
                            resources_status[c['resource']] = None
                    current_task[i]['arrival'] += current_task[i]['period']
                    current_task[i]['deadline'] += current_task[i]['period']
                    current_task[i]['remaining_time'] = current_task[i]['wcet']
                    current_task[i] = None
                    num_schedulable += 1
                break 

            pi = max([ceilings[r] for r in range(num_resources) if resources_status[r] is not None], default=0)
        status, failed = check_deadlines(processors, time)
        if status:
            for i, p in enumerate(processors):
                if current_task[i] in failed:
                    current_task[i] = None 
            for t in failed:
                num_non_scheduleable += 1
                for c in t['criticality']:
                    if resources_status[c['resource']] == t['id']:
                        resources_status[c['resource']] = None
                t['arrival'] += t['period']
                t['deadline'] += t['period']
                t['remaining_time'] = t['wcet']
        time += 1
    return num_schedulable, num_non_scheduleable


        