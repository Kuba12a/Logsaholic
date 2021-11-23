from fastapi import FastAPI
from pydantic import BaseModel
import click
import datetime


class Alert(BaseModel):
    source: str
    alert_id: int
    date: datetime.datetime
    message: str


app = FastAPI()


@app.post("/alert")
def login(alert: Alert):
    print(f"Alert!\nSource: {alert.source}\nAlertId: {alert.alert_id}\nDate: {alert.date.strftime('%m/%d/%Y, %H:%M:%S')}\nMessage: {alert.message}")
    return {"msg": "alert send successfully"}
