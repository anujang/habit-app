import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb", region_name="eu-west-2")
table = dynamodb.Table("Reminders")

def save_reminder(user_id: str, content: str, remind_at: str):
    reminder_id = str(uuid.uuid4())
    table.put_item(Item={
        "user_id": user_id,
        "reminder_id": reminder_id,
        "content": content,
        "remind_at": remind_at,
        "created_at": datetime.utcnow().isoformat()
    })
    return reminder_id
    