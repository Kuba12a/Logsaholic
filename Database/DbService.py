import sqlite3
from pydantic import BaseModel
import datetime

conn = sqlite3.connect('events.db')


class Event(BaseModel):
    event_id: int
    source: str
    date: datetime.datetime
    message: str



c = conn.cursor()


def insert_event(event: Event):
    with conn:
        c.execute(
            f"INSERT INTO events VALUES ('{event.event_id}', '{event.source}', '{event.date.strftime('%m/%d/%Y, %H:%M:%S')}', '{event.message}')")

def select_events():
    with conn:
        c.execute(
            "SELECT * from events")
    return c.fetchall()
