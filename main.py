from business.webhook import create_event

def test_lambda_handler(): 
    create_event(
        {
            "event": "taskCreated",
            "history_items": [
                {
                    "id": "2800763136717140857",
                    "type": 1,
                    "date": "1642734631523",
                    "field": "status",
                    "parent_id": "162641062",
                    "data": {
                        "status_type": "open"
                    },
                    "source": None,
                    "user": {
                        "id": 183,
                        "username": "John",
                        "email": "john@company.com",
                        "color": "#7b68ee",
                        "initials": "J",
                        "profilePicture": None
                    },
                    "before": {
                        "status": None,
                        "color": "#000000",
                        "type": "removed",
                        "orderindex": -1
                    },
                    "after": {
                        "status": "to do",
                        "color": "#f9d900",
                        "orderindex": 0,
                        "type": "open"
                    }
                },
                {
                    "id": "2800763136700363640",
                    "type": 1,
                    "date": "1642734631523",
                    "field": "task_creation",
                    "parent_id": "162641062",
                    "data": {},
                    "source": None,
                    "user": {
                        "id": 183,
                        "username": "John",
                        "email": "john@company.com",
                        "color": "#7b68ee",
                        "initials": "J",
                        "profilePicture": None
                    },
                    "before": None,
                    "after": None
                }
            ],
            "task_id": "1vj37mc",
            "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204"
        }
    )

test_lambda_handler()