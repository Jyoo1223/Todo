def add_task(tasks,new_task):
    if new_task:
        tasks.append(new_task)
    return tasks

def remove_task(tasks,index):
    if 0<=index<len(tasks):
        tasks.pop(index)
    return tasks
