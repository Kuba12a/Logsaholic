from pydantic import BaseModel
import datetime

class Alert(BaseModel):
    source: str
    alert_id: int
    date: str
    message: str