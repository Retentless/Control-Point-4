from uuid import uuid4

import uuid

def create_task(description, tags):
    unique_tags = []
    for tag in tags:
        if tag not in unique_tags:
            unique_tags.append(tag)
    
    return {
        'id': None,
        'description': description,
        'completed': False,
        'tags': unique_tags
    }


def add_task(tasks, task):
    new_task = task.copy()
    
    if new_task['id'] is None:
        if not tasks:
            new_task['id'] = 1
        else:
            max_id = max(t['id'] for t in tasks)
            new_task['id'] = max_id + 1
    
    tasks.append(new_task)
    return tasks


def add_tag_to_task(tasks, task_id, tag):
    for task in tasks:
        if task['id'] == task_id:
            if tag not in task['tags']:
                task['tags'].append(tag)
            break
    return tasks


def remove_tag_from_task(tasks, task_id, tag):
    for task in tasks:
        if task['id'] == task_id:
            if tag in task['tags']:
                task['tags'].remove(tag)
            break
    return tasks


def mark_task_completed(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return tasks


def filter_tasks_by_tags(tasks, filter_tags=None):
    if not filter_tags:
        return tasks.copy()
    
    return [
        task.copy()
        for task in tasks
        if all(tag in task['tags'] for tag in filter_tags)
    ]