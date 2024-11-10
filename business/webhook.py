import datetime
import json
import clickup.task
import db.event

def _create_task_created_event(event: dict):
    print("Handling taskCreated event")
    
    for item in event["history_items"]:
        if item["field"] == 'task_creation':
            task = clickup.task.get(event["task_id"])

            db.event.insert(
                service='clickup',
                type='task',
                content=f'{item["user"]["username"]} created the task "{event["task_id"]} - {task["name"]}" with status "{task["status"]["status"]}".',
                timestamp=datetime.datetime.fromtimestamp(int(item["date"]) / 1000),
                url=f'https://app.clickup.com/t/{event["task_id"]}',
            )

def _create_task_status_updated_event(event: dict):
    print("Handling statusUpdated event")
    
    for item in event["history_items"]:
        if item["field"] == 'status':
            task = clickup.task.get(event["task_id"])

            db.event.insert(
                service='clickup',
                type='task',
                content=f'{item["user"]["username"]} changed the task "{event["task_id"]} - {task["name"]}" status from "{item["before"]["status"]}" to "{item["after"]["status"]}".',
                timestamp=datetime.datetime.fromtimestamp(int(item["date"]) / 1000),
                url=f'https://app.clickup.com/t/{event["task_id"]}',
            )

def _create_task_assignee_updated_event(event: dict):
    print("Handling assigneeUpdated event")
    
    for item in event["history_items"]:
        task = clickup.task.get(event["task_id"])

        if item["before"] and item["after"]:
            db.event.insert(
                service='clickup',
                type='task',
                content=f'{item["user"]["username"]} the task "{event["task_id"]} - {task["name"]}" assignee from "{item["before"]["username"]}" to "{item["after"]["username"]}".',
                timestamp=datetime.datetime.fromtimestamp(int(item["date"]) / 1000),
                url=f'https://app.clickup.com/t/{event["task_id"]}',
            )
        elif item["before"]:
            db.event.insert(
                service='clickup',
                type='task',
                content=f'{item["user"]["username"]} removed "{item["before"]["username"]}" as assignee from the task "{event["task_id"]} - {task["name"]}".',
                timestamp=datetime.datetime.fromtimestamp(int(item["date"]) / 1000),
                url=f'https://app.clickup.com/t/{event["task_id"]}',
            )
        else:
            db.event.insert(
                service='clickup',
                type='task',
                content=f'{item["user"]["username"]} add "{item["after"]["username"]}" as assignee to the task "{event["task_id"]} - {item["name"]}".',
                timestamp=datetime.datetime.fromtimestamp(int(item["date"]) / 1000),
                url=f'https://app.clickup.com/t/{event["task_id"]}',
            )

def _create_task_comment_posted_event(event: dict):
    print("Handling commentPosted event")
    
    for item in event["history_items"]:
        if item["field"] == 'comment':
            task = clickup.task.get(event["task_id"])

            db.event.insert(
                service='clickup',
                type='task',
                content=f'{item["user"]["username"]} commented "{item["comment"]["text_content"]}" on task "{event["task_id"]} - {task["name"]}".',
                timestamp=datetime.datetime.fromtimestamp(int(item["date"]) / 1000),
                url=f'https://app.clickup.com/t/{event["task_id"]}',
            )


def create_event(event: dict):
    print("Checking event type")

    match event["event"]:
        case 'taskCreated':
            _create_task_created_event(event)
        # case 'taskDeleted':
        #    _create_task_deleted_event(event)
        # case 'taskPriorityUpdated':
        #    _create_task_priority_updated_event(event)
        case 'taskStatusUpdated':
            _create_task_status_updated_event(event)
        case 'taskAssigneeUpdated':
            _create_task_assignee_updated_event(event)
        # case 'taskDueDateUpdated':
        #    _create_task_due_date_updated_event(event)
        case 'taskCommentPosted':
            _create_task_comment_posted_event(event)
        # case 'taskTimeEstimateUpdated':
        #    _create_task_time_estimate_update_event(event)
        # case 'taskTimeTrackedUpdated':
        #    _create_task_time_tracked_update_event(event)
        case _:
            print(f"{event['event']} event cannot be handled.")
