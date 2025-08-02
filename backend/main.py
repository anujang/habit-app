from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import save_reminder

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello from the backend"}

class ReminderRequest(BaseModel):
    user_id: str
    content: str
    remind_at: str

@app.post("/reminders")
def create_reminder(reminder: ReminderRequest):
    try:
        reminder_id = save_reminder(
            user_id=reminder.user_id,
            content=reminder.content,
            remind_at=reminder.remind_at
        )
        return {"reminder_id":reminder_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))